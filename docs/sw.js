// Network first, falling back to the last saved copy, so Wonderbook still opens offline.
const CACHE = 'wonderbook-v2';
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));
self.addEventListener('fetch', e => {
  const u = new URL(e.request.url);
  if (e.request.method !== 'GET' || u.hostname.includes('anthropic.com') || u.hostname.includes('open-meteo.com') || u.hostname.includes('github.com')) return;
  e.respondWith(fetch(e.request).then(r => { const c = r.clone(); caches.open(CACHE).then(x => x.put(e.request, c)).catch(() => {}); return r; }).catch(() => caches.match(e.request)));
});
