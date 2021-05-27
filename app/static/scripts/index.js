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
    var rows = document.getElementById("data").rows;
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
    var csvFile = csvFile = new Blob(["\ufeff" + csv], {type: "text/csv"});
    var downloadLink = downloadLink = document.createElement("a");
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

// confetti !!!!!!!!!!!!!!!!!!!
const partyBtn = document.getElementById("party");
let party = false;

partyBtn.addEventListener("click", () => {
  const container = tsParticles.domItem(0);

  if (!party) {
    party = true;

    container.playEmitter("party");

    partyBtn.innerText = partyBtn.innerText.replace("Start", "Stop");
  } else {
    party = false;

    container.pauseEmitter("party");

    partyBtn.innerText = partyBtn.innerText.replace("Stop", "Start");
  }
});

tsParticles.load("tsparticles", {
  fpsLimit: 60,
  fullScreen: {
    enable: true
  },
  particles: {
    number: {
      value: 0,
      zIndex: 100
    },
    color: {
      value: ["#00FFFC", "#FC00FF", "#fffc00"]
    },
    shape: {
      type: "confetti",
      options: {
        confetti: {
          type: ["circle", "square"]
        }
      }
    },
    opacity: {
      value: 1,
      animation: {
        enable: true,
        minimumValue: 0,
        speed: 2,
        startValue: "max",
        destroy: "min"
      }
    },
    size: {
      value: 7,
      random: {
        enable: true,
        minimumValue: 3
      }
    },
    links: {
      enable: false
    },
    life: {
      duration: {
        sync: true,
        value: 5
      },
      count: 1
    },
    move: {
      enable: true,
      gravity: {
        enable: true,
        acceleration: 20
      },
      speed: 20,
      decay: 0.1,
      direction: "none",
      random: false,
      straight: false,
      outModes: {
        default: "destroy",
        top: "none"
      }
    }
  },
  interactivity: {
    detectsOn: "window",
    events: {
      resize: true
    }
  },
  detectRetina: true,
  emitters: {
    autoPlay: false,
    name: "party",
    direction: "none",
    spawnColor: {
      value: "#ff0000",
      animation: {
        h: {
          enable: true,
          offset: {
            min: -1.4,
            max: 1.4
          },
          speed: 0.1,
          sync: false
        },
        l: {
          enable: true,
          offset: {
            min: 20,
            max: 80
          },
          speed: 0,
          sync: false
        }
      }
    },
    life: {
      count: 0,
      duration: 0.1,
      delay: 0.4
    },
    rate: {
      delay: 0.1,
      quantity: 100
    },
    size: {
      width: 0,
      height: 0
    }
  }
});
