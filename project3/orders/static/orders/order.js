document.addEventListener('DOMContentLoaded', ()=> {
  document.querySelector('#sidenav').style.display = 'none';
  document.querySelector('#subs').style.display = 'block';
  document.querySelector('#regular_pizza').style.display = 'block';
  document.querySelector('#sicilian_pizza').style.display = 'block';
  document.querySelector('#salad').style.display = 'block';
  document.querySelector('#dinner_platters').style.display = 'block';
  document.querySelector('#pasta').style.display = 'block';
});

document.getElementById('full_menu').addEventListener("click", ()=>{
  document.querySelector('#subs').style.display = 'block';
  document.querySelector('#regular_pizza').style.display = 'block';
  document.querySelector('#sicilian_pizza').style.display = 'block';
  document.querySelector('#salad').style.display = 'block';
  document.querySelector('#dinner_platters').style.display = 'block';
  document.querySelector('#pasta').style.display = 'block';
});

document.getElementById('reg_pizza').addEventListener("click", ()=>{
  document.querySelector('#subs').style.display = 'none';
  document.querySelector('#regular_pizza').style.display = 'block';
  document.querySelector('#sicilian_pizza').style.display = 'none';
  document.querySelector('#salad').style.display = 'none';
  document.querySelector('#dinner_platters').style.display = 'none';
  document.querySelector('#pasta').style.display = 'none';
});

document.getElementById('sic_pizza').addEventListener("click", ()=>{
  document.querySelector('#subs').style.display = 'none';
  document.querySelector('#regular_pizza').style.display = 'none';
  document.querySelector('#sicilian_pizza').style.display = 'block';
  document.querySelector('#salad').style.display = 'none';
  document.querySelector('#dinner_platters').style.display = 'none';
  document.querySelector('#pasta').style.display = 'none';
});

document.getElementById('sub_menu').addEventListener("click", ()=>{
  document.querySelector('#subs').style.display = 'block';
  document.querySelector('#regular_pizza').style.display = 'none';
  document.querySelector('#sicilian_pizza').style.display = 'none';
  document.querySelector('#salad').style.display = 'none';
  document.querySelector('#dinner_platters').style.display = 'none';
  document.querySelector('#pasta').style.display = 'none';
});

document.getElementById('salad_menu').addEventListener("click", ()=>{
  document.querySelector('#salad').style.display = 'block';
  document.querySelector('#regular_pizza').style.display = 'none';
  document.querySelector('#sicilian_pizza').style.display = 'none';
  document.querySelector('#subs').style.display = 'none';
  document.querySelector('#dinner_platters').style.display = 'none';
  document.querySelector('#pasta').style.display = 'none';
});

document.getElementById('pasta_menu').addEventListener("click", ()=>{
  document.querySelector('#salad').style.display = 'none';
  document.querySelector('#regular_pizza').style.display = 'none';
  document.querySelector('#sicilian_pizza').style.display = 'none';
  document.querySelector('#subs').style.display = 'none';
  document.querySelector('#dinner_platters').style.display = 'none';
  document.querySelector('#pasta').style.display = 'block';
});

document.getElementById('platter_menu').addEventListener("click", ()=>{
  document.querySelector('#salad').style.display = 'none';
  document.querySelector('#regular_pizza').style.display = 'none';
  document.querySelector('#sicilian_pizza').style.display = 'none';
  document.querySelector('#subs').style.display = 'none';
  document.querySelector('#dinner_platters').style.display = 'block';
  document.querySelector('#pasta').style.display = 'none';
});
