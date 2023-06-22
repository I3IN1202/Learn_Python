function checkProtocol(url) {
    const protocol = new URL(url).protocol;
    if (protocol === 'http:' || protocol === 'https:') {
        return true;
    } else {
        return false;
    }
}