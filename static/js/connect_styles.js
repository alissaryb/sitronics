const cssFiles = ['/static/css/body.css', '/static/css/button.css', '/static/css/nav.css', '/static/css/card.css'];

cssFiles.forEach(file => {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = file;
    document.head.appendChild(link);
});