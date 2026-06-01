import { getAssetFromKV } from '@cloudflare/kv-asset-handler';

addEventListener('fetch', event => {
  event.respondWith(handleEvent(event));
});

async function handleEvent(event) {
  try {
    const options = {
      mapRequestToAsset: req => {
        let url = new URL(req.url);
        if (url.pathname === '/') {
          url.pathname = '/index.html';
        }
        return new Request(url.toString(), req);
      },
    };
    return await getAssetFromKV(event, options);
  } catch (e) {
    return new Response('Not found', { status: 404 });
  }
}
