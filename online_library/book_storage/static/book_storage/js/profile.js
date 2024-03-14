function confirmLogout() {
    var logoutUrl = document.querySelector('.logout-link').getAttribute('data-logout-url');
    var isConfirmed = confirm("Вы уверены, что хотите выйти из аккаунта?");
    
    if (isConfirmed) {
        window.location.href = logoutUrl;
    } 
}