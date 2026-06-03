export default {
  async fetch(request, env) {
    // let's make all the domains move to one place...
    const url = new URL(request.url)
    switch (url.hostname) {
      case 'ruzena.uk':
      case 'ruzena.co.uk':
      case 'rachellevy.uk':
        url.hostname = 'rachellevy.org.uk'
        return Response.redirect(url.toString(), 302)
    }
    // and now service the domain...
    try {
      return await env.ASSETS.fetch(request)
    } catch (err) {
      return new Response('Not found', { status: 404 })
    }
  }
}
