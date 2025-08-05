var timeout = 15000;

window.setTimeout(poller, timeout);

function poller() {
    // Update this URL to point to your kitchen endpoint
    // Replace 'yourusername' with your actual PythonAnywhere username
    window.location = window.location.origin + "/kitchen/";

    window.setTimeout(poller, timeout);
}
