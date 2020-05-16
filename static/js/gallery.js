const prev = document.querySelector('#prev');
const next = document.querySelector('#next');
const els = document.querySelectorAll("[type='radio']");

const changingInterval = 5000; //milliseconds
var timeToNextPicture = Date.now() + changingInterval;


function simulateClick(id) {
    var evt = document.createEvent("MouseEvents");
    evt.initMouseEvent("click", true, true, window, 1, 0, 0, 0, 0,
        false, false, false, false, 0, null);

    var cb = document.getElementById(id);
    cb.dispatchEvent(evt);
}

function resolveAfter2Seconds() {
    return new Promise(resolve => {
        setTimeout(() => {
            if (Date.now() > timeToNextPicture) simulateClick('next')
            resolve();
        }, 1000);
    });
}

async function asyncCall() {
    while (true) {
        await resolveAfter2Seconds();
    }
}

asyncCall();

// prev & next button
prev.addEventListener('click', () => {
    for (var i = 0; i < els.length; i++) {
        if (els[i].checked) {
            if (i === 0) {
                els[els.length - 1].checked = true;
                reorder(els[els.length - 1], els);
            } else {
                els[i - 1].checked = true;
                reorder(els[i - 1], els);
            }
            break;
        }
    }
    timeToNextPicture = Date.now() + changingInterval;
});

next.addEventListener('click', () => {
    for (var i = els.length - 1; i >= 0; i--) {
        if (els[i].checked) {
            if (i === els.length - 1) {
                els[0].checked = true;
                reorder(els[0], els);
            } else {
                els[i + 1].checked = true;
                reorder(els[i + 1], els);
            }
            break;
        }
    }
    timeToNextPicture = Date.now() + changingInterval;
});

// main logic
for (const el of els)
    el.addEventListener("input", e => reorder(e.target, els));
reorder(els[0], els);

function reorder(targetEl, els) {
    const nItems = els.length;
    let processedUncheck = 0;
    for (const el of els) {
        const containerEl = el.nextElementSibling;
        if (el === targetEl) { //checked radio
            containerEl.style.setProperty("--w", "100%");
            containerEl.style.setProperty("--l", "0");
        } else { //unchecked radios
            containerEl.style.setProperty("--w", `${100/(nItems-1)}%`);
            containerEl.style.setProperty("--l", `${processedUncheck * 100/(nItems-1)}%`);
            processedUncheck += 1;
        }
    }
    timeToNextPicture = Date.now() + changingInterval;
}


//FROM HERE NEW SCRIPT FOR THE GALLERY
// applying photobox on a `gallery` element which has lots of thumbnails links.
// Passing options object as well:
//-----------------------------------------------
$('#gallery').photobox('a', { time: 0 });

// using a callback and a fancier selector
//----------------------------------------------
$('#gallery').photobox('li > a.family', { time: 0 }, callback);

function callback() {
    console.log('image has been loaded');
}

// destroy the plugin on a certain gallery:
//-----------------------------------------------
$('#gallery').photobox('destroy');

// re-initialize the photbox DOM (does what Document ready does)
//-----------------------------------------------
$('#gallery').photobox('prepareDOM');