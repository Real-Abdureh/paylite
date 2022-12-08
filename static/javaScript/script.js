function generatePDF(){
    const element = document.getElementById("invoice");
    alert('A copy of the receipt has been sent to your E-mail.')

    html2pdf()
    .from(element)
    .save();
}