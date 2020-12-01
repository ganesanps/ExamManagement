window.onload=function()
{
   const toggleBtn=document.getElementsByClassName("ham")[0];
   const navBar1=document.getElementsByClassName("nav1")[0].getElementsByTagName("ul")[0];
   const toggleBtn2=document.getElementsByClassName("profile")[0];
   const navBar2=document.getElementsByClassName("nav2")[0].getElementsByTagName("ul")[0];
   const btn = document.getElementById("dark");
   console.log(btn);
   btn.addEventListener('click', () => {
      document.body.classList.toggle("dark");
   })
   toggleBtn.addEventListener("click",() => {

      navBar1.classList.toggle("active");

   });
   
   toggleBtn2.addEventListener("click",() => {

    console.log(navBar2);
    navBar2.classList.toggle("active");

 });
}