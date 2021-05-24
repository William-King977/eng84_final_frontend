//topButton
var topbutton = document.getElementById('topBtn');
window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        topbutton.style.display = 'block';
    } else {
        topbutton.style.display = 'none';
    }
}

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}


// Converts the table into a list of values
function exportTableToCSV(filename) {
    var csv = [];
    var rows = document.getElementById("jobs-table").rows;
    for (var i = 0; i < rows.length; i++) {
        var row = []
        var cols = rows[i].querySelectorAll("td, th");
        for (var j = 0; j < cols.length; j++) 
            row.push(`"${cols[j].innerText}"`);
        csv.push(row.join(","));   
    }
    // Download CSV file
    downloadCSV(csv.join("\n"), filename);
}

// Converts list into a CSV file
function downloadCSV(csv, filename) {
    var csvFile;
    var downloadLink;
    // CSV file
    csvFile = new Blob(["\ufeff" + csv], {type: "text/csv"});
    // Download link
    downloadLink = document.createElement("a");
    // File name
    downloadLink.download = filename;
    // Create a link to the file
    downloadLink.href = window.URL.createObjectURL(csvFile);
    // Hide download link
    downloadLink.style.display = "none";
    // Add the link to DOM
    document.body.appendChild(downloadLink);
    // Click download link
    downloadLink.click();
}