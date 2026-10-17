"""Shared search metadata, using only verified site information."""
from html import escape

def enrich(graph, origin, route, title, description, pages, post=None):
    entity, person, page = graph[:3]
    website_id = origin + '/#website'
    entity['logo'] = {'@type': 'ImageObject', 'url': origin + '/assets/sitesutra-logo.svg'}
    graph.append({'@type': 'WebSite', '@id': website_id, 'url': origin + '/', 'name': 'SiteSutra', 'publisher': {'@id': entity['@id']}, 'inLanguage': 'en-IN'})
    page.update({'isPartOf': {'@id': website_id}, 'description': description, 'inLanguage': 'en-IN'})
    if route == '/contact/': page['@type'] = 'ContactPage'
    if route != '/':
        parents = ['/']
        parts = route.strip('/').split('/')
        for n in range(1, len(parts)):
            parent = '/' + '/'.join(parts[:n]) + '/'
            if parent in pages: parents.append(parent)
        parents.append(route)
        labels = {'/': 'Home', '/services/': 'Services', '/work/': 'Work', '/guides/': 'Buyer guides', '/blog/': 'Blog'}
        breadcrumb_id = origin + route + '#breadcrumb'
        graph.append({'@type': 'BreadcrumbList', '@id': breadcrumb_id, 'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'name': labels.get(r, pages[r][0]), 'item': origin + r}
            for i, r in enumerate(parents)]})
        page['breadcrumb'] = {'@id': breadcrumb_id}
    tags = {'og:site_name': 'SiteSutra', 'og:title': title + ' | SiteSutra', 'og:description': description,
            'og:url': origin + route, 'og:type': 'article' if post else 'website', 'og:locale': 'en_IN',
            'og:image': origin + '/assets/social-card.png', 'og:image:width': '1200', 'og:image:height': '630',
            'og:image:alt': 'SiteSutra — founder-led websites, design and search marketing in Varanasi'}
    if post: tags['article:published_time'] = post['date']
    result = '<meta name="robots" content="index,follow,max-image-preview:large">'
    result += ''.join('<meta property="' + k + '" content="' + escape(v, quote=True) + '">' for k, v in tags.items())
    result += '<meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/assets/sitesutra-logo.svg" type="image/svg+xml">'
    return result
