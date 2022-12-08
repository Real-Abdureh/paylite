let btnSendGreen = document.getElementById('b1Green');
let messageGreen = document.querySelector('b');

btnSendGreen.addEventListener('click', () =>{
    btnSendGreen.innerText= '...';

    setTimeout(() => {
        btnSendGreen.style.display = "none";
        btnSendRed.style.display = "none";
        messageGreen.innerText = 'Completed';
    }, 1000);
});

let btnSendRed = document.getElementById('b1Red');
let messageRed = document.querySelector('b');

btnSendRed.addEventListener('click', ()=>{

    setTimeout(() => {
        btnSendGreen.style.display = "none";
        btnSendRed.style.display = "none";
        messageRed.innerText = 'Cancelled';
    }, 1000);
});
