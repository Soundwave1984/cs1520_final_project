// Auto-redirect to main menu after 15 seconds
setTimeout(function() {
    // Extract table number from current URL
    const currentPath = window.location.pathname;
    const tableMatch = currentPath.match(/\/order\/(\d+)/);
    
    if (tableMatch) {
        const tableNumber = tableMatch[1];
        // Redirect to main menu with table number
        window.location.href = `/${tableNumber}`;
    } else {
        // Fallback redirect to table 1 if can't determine table number
        window.location.href = '/1';
    }
}, 15000);