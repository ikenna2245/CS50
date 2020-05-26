document.addEventListener ('DOMContentLoaded', ()=> {
  document.querySelector('#create').onclick = ()=> {
    document.querySelector('.model').style.display = "none";
    document.querySelector('.form1').style.display= 'none';
    document.querySelector('.form').style.display= 'block';

  }
});

document.addEventListener ('DOMContentLoaded', ()=>{
  document.querySelector('#form').onsubmit = () => {
    const request = new XMLHttpRequest();
    const channel = document.querySelector('#text').value;
    request.open ('POST', '/home');
    request.onload = () => {
      const data = JSON.parse (request.responseText);
      if (data.success) {
        const result = `#${channel} has been created`
        document.querySelector('#result').innerHTML = result;
      }
      else {
        document.querySelector('#result').innerHTML = "Channel already exist.";
      }
    }
    const data = new FormData();
    data.append ('channel', channel);
    request.send(data)
    document.querySelector('#text').value = '';
    document.querySelector('.form').style.display= 'none';
    window.location.reload(true);
    return false;
  };
});

document.addEventListener('DOMContentLoaded', ()=>{
  document.querySelector('#join').onclick = ()=> {
    document.querySelector ('.model').style.display = "flex";
    document.querySelector('.form').style.display= 'none';
    document.querySelector('.form1').style.display= 'none';
  };
});

document.addEventListener ('DOMContentLoaded', ()=> {
  document.querySelector('#change').onclick = ()=> {
    document.querySelector('.model').style.display = "none";
    document.querySelector('.form1').style.display= 'block';
    document.querySelector('.form').style.display= 'none';
  }
});
