/* Progressive enhancement. No tracking, no third-party scripts. */
(() => {
  'use strict';
  const root = document.documentElement;
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const menu = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#main-nav');
  const closeMenu = (restoreFocus = false) => {
    nav?.classList.remove('is-open');
    menu?.setAttribute('aria-expanded', 'false');
    if (restoreFocus) menu?.focus();
  };
  menu?.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    nav?.classList.toggle('is-open', open);
  });
  nav?.querySelectorAll('a').forEach(a => a.addEventListener('click', () => closeMenu()));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menu?.getAttribute('aria-expanded') === 'true') closeMenu(true);
  });
  document.addEventListener('click', event => {
    if (menu?.getAttribute('aria-expanded') === 'true' && !event.target.closest('.site-header')) closeMenu();
  });
  const desktop = window.matchMedia('(min-width: 701px)');
  desktop.addEventListener('change', () => closeMenu());

  document.querySelectorAll('.portrait-window img, .story-photo img').forEach(image => {
    const unavailable = () => {
      const frame = image.parentElement;
      image.hidden = true;
      frame.classList.add('image-unavailable');
      if (!frame.querySelector('.image-fallback-message')) {
        const message = document.createElement('p');
        message.className = 'image-fallback-message';
        message.textContent = 'Portrait temporarily unavailable';
        frame.append(message);
      }
    };
    image.addEventListener('error', unavailable, {once: true});
    if (image.complete && image.naturalWidth === 0) unavailable();
  });

  const progress = document.querySelector('.reading-progress');
  let queued = false;
  const updateProgress = () => {
    const height = root.scrollHeight - root.clientHeight;
    if (progress && !motion.matches) progress.style.transform = `scaleX(${height > 0 ? Math.max(0, Math.min(1, root.scrollTop / height)) : 0})`;
    queued = false;
  };
  window.addEventListener('scroll', () => {
    if (!queued) { queued = true; requestAnimationFrame(updateProgress); }
  }, {passive: true});
  updateProgress();

  if (!motion.matches && 'IntersectionObserver' in window) {
    root.classList.add('motion-ready');
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target);
      }
    }, {threshold: 0.04, rootMargin: '0px 0px 40px 0px'});
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
    motion.addEventListener('change', () => {
      if (motion.matches) { observer.disconnect(); root.classList.remove('motion-ready'); }
    });
  }

  const stages = {
    rees: {
      bronze: ['HISTORICAL DATA PROCESSING', '411,709,736', 'Raw events ingested across seven monthly partitions. This is pipeline volume, separate from model training.'],
      silver: ['CANONICAL EVENTS', '410,325,314', 'Exact deduplication removed 1,384,422 events. Silver is the clean data foundation for Gold.'],
      gold: ['BOUNDED SESSION AGGREGATION', '7 months. 64 buckets.', 'Monthly Gold outputs are restartable. Within each month, sessions are hashed into 64 buckets before ordered aggregation.'],
      ranker: ['SEPARATE OFFLINE TEST', '0.02443 → 0.03556', 'MRR@20: popularity to purchase ranker. 1,499,021 training interactions and 5,000 held-out test users.']
    },
    fulfill: {
      ci: ['BUILD & PROMOTION', 'Keyless CI.', 'GitHub Actions uses OIDC / Workload Identity Federation, scans an image, and promotes its exact digest.'],
      gitops: ['DEPLOYMENT CONTROLLER', 'Git is desired state.', 'Argo CD reconciles the Helm-managed API. Actions builds and promotes; Argo CD owns normal deployment.'],
      runtime: ['CONTROLLED CLOUD LAB', 'GKE Autopilot.', 'Terraform provisions the lab. Recorded cloud checks cover API health, metrics and delivery, not the complete data stack.'],
      observe: ['MONITORING & RECOVERY', 'Diagnose. Restore.', 'Prometheus, Grafana and Alertmanager support the lab. A deliberate ImagePullBackOff exercise is documented with recovery.']
    }
  };
  document.querySelectorAll('[data-system]').forEach(map => {
    map.querySelectorAll('[data-stage]').forEach(button => button.addEventListener('click', () => {
      const value = stages[map.dataset.system]?.[button.dataset.stage];
      if (!value) return;
      map.querySelectorAll('[data-stage]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      map.querySelector('[data-stage-label]').textContent = value[0];
      map.querySelector('[data-stage-value]').textContent = value[1];
      map.querySelector('[data-stage-description]').textContent = value[2];
    }));
  });

  const filters = document.querySelectorAll('[data-filter]');
  const projects = document.querySelectorAll('[data-category]');
  const count = document.querySelector('[data-filter-count]');
  filters.forEach(button => button.addEventListener('click', () => {
    filters.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    let visible = 0;
    projects.forEach(project => {
      project.hidden = button.dataset.filter !== 'all' && !project.dataset.category.split(' ').includes(button.dataset.filter);
      if (!project.hidden) { visible += 1; project.classList.add('in-view'); }
    });
    if (count) count.textContent = `${visible} ${visible === 1 ? 'project' : 'projects'}`;
  }));

  const portrait = document.querySelector('[data-parallax]');
  const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');
  let pointerQueued = false;
  let x = 0, y = 0;
  const resetPortrait = () => {
    portrait?.style.removeProperty('--portrait-x');
    portrait?.style.removeProperty('--portrait-y');
  };
  portrait?.addEventListener('pointermove', event => {
    if (motion.matches || !finePointer.matches) return;
    const bounds = portrait.getBoundingClientRect();
    x = (event.clientX - bounds.left) / bounds.width - 0.5;
    y = (event.clientY - bounds.top) / bounds.height - 0.5;
    if (!pointerQueued) {
      pointerQueued = true;
      requestAnimationFrame(() => {
        if (!motion.matches) {
          portrait.style.setProperty('--portrait-x', `${(x * 7).toFixed(1)}px`);
          portrait.style.setProperty('--portrait-y', `${(y * 7).toFixed(1)}px`);
        }
        pointerQueued = false;
      });
    }
  });
  portrait?.addEventListener('pointerleave', resetPortrait);
  motion.addEventListener('change', resetPortrait);
})();
