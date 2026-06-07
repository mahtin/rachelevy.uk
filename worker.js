export default {
  async fetch(request, env) {
    // let's make all the domains move to one place...
    const url = new URL(request.url);
    switch (url.hostname) {
      case 'ruzena.uk':
      case 'ruzena.co.uk':
      case 'rachellevy.uk':
        url.hostname = 'rachellevy.org.uk';
        return Response.redirect(url.toString(), 302);
    }
    // and now service the domain...
    try {
      return await env.ASSETS.fetch(request);
    } catch (err) {
      // return new Response('Not found', { status: 404 });
      const url = new URL(request.url);
      const errorRequest = new Request(`${url.origin}/404.html`, request);
      try {
        const notFoundResponse = await env.ASSETS.fetch(errorRequest);
        // Return the 404.html contents with an explicit 404 status code
        return new Response(notFoundResponse.body, {
          ...notFoundResponse,
          status: 404,
          headers: {
            ...notFoundResponse.headers,
            'content-type': 'text/html; charset=utf-8'
          }
        });
      } catch (notFoundError) {
        // Fallback if the 404.html file itself is missing from storage
        return new Response("404 Not Found", { status: 404 });
      }
    }
  }
}
