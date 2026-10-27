(() => {
  const header = document.querySelector('.site-header');
  const nav = header?.querySelector('nav');

  if (header && nav) {
    nav.id ||= 'primary-nav';
    nav.setAttribute('aria-label', 'Main navigation');
    let menu = header.querySelector('.menu-toggle');
    if (!menu) {
      menu = document.createElement('button');
      menu.type = 'button';
      menu.className = 'menu-toggle';
      header.insertBefore(menu, nav);
    }
    menu.hidden = false;
    menu.setAttribute('aria-controls', nav.id);
    const closeMenu = () => {
      header.classList.remove('is-menu-open');
      menu.setAttribute('aria-expanded', 'false');
      menu.textContent = 'Menu';
    };
    closeMenu();
    header.classList.add('is-enhanced');
    menu.addEventListener('click', () => {
      const open = header.classList.toggle('is-menu-open');
      menu.setAttribute('aria-expanded', String(open));
      menu.textContent = open ? 'Close' : 'Menu';
    });
    header.addEventListener('keydown', event => {
      if (event.key === 'Escape' && header.classList.contains('is-menu-open')) {
        closeMenu();
        menu.focus();
      }
    });
    nav.addEventListener('click', event => {
      if (event.target.closest('a')) closeMenu();
    });
    document.addEventListener('click', event => {
      if (!header.contains(event.target)) closeMenu();
    });
    header.addEventListener('focusout', event => {
      if (!header.contains(event.relatedTarget)) closeMenu();
    });
    window.matchMedia('(max-width: 800px)').addEventListener('change', closeMenu);
  }

  const tablist = document.querySelector('.workflow-tabs');
  const tabs = [...document.querySelectorAll('[data-workflow]')];
  if (tablist && tabs.length) {
    tablist.setAttribute('role', 'tablist');
    const panels = tabs.map(tab => document.getElementById(`workflow-${tab.dataset.workflow}`));
    const selectTab = (index, focus = false) => {
      tabs.forEach((tab, i) => {
        tab.setAttribute('aria-selected', String(i === index));
        tab.tabIndex = i === index ? 0 : -1;
        panels[i].hidden = i !== index;
      });
      if (focus) tabs[index].focus();
    };
    tabs.forEach((tab, index) => {
      tab.setAttribute('role', 'tab');
      tab.setAttribute('aria-controls', panels[index].id);
      panels[index].setAttribute('role', 'tabpanel');
      panels[index].setAttribute('aria-labelledby', tab.id);
      panels[index].tabIndex = 0;
      tab.addEventListener('click', event => {
        event.preventDefault();
        selectTab(index);
      });
      tab.addEventListener('keydown', event => {
        if (event.key === ' ' || event.key === 'Enter') {
          event.preventDefault();
          selectTab(index);
          return;
        }
        let next;
        if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
        if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
        if (event.key === 'Home') next = 0;
        if (event.key === 'End') next = tabs.length - 1;
        if (next !== undefined) {
          event.preventDefault();
          selectTab(next, true);
        }
      });
    });
    const followHash = () => {
      const index = panels.findIndex(panel => `#${panel.id}` === window.location.hash);
      if (index !== -1) selectTab(index);
    };
    selectTab(0);
    followHash();
    window.addEventListener('hashchange', followHash);
  }

  if (document.body.classList.contains('home') && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    }, { threshold: 0.08 });
    for (const element of document.querySelectorAll('.section-top, .connected-grid, .process-grid > li, .trust-grid, .faq-layout, .contact-grid')) {
      if (element.getBoundingClientRect().top < window.innerHeight) continue;
      element.classList.add('reveal-ready');
      observer.observe(element);
    }
  }
})();
