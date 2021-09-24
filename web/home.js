

eel.expose(print)
function printnow(print){
    eel.printnow(print);
}

// open overlay
function openCreate() {
    document.getElementById("myNav").style.width = "100%";
}

function closeCreate() {
    document.getElementById("myNav").style.width = "0%";
}

function startPython(){
    eel.start()
  }

  function stopPython(){
    eel.stop()
  }



  function savePython(){
    var x = document.getElementById("textout").value;
    eel.save(x);
  }
  function copyPython(){
    eel.copy()
    eel.copy()
  }
  eel.expose(setstatus);
  function setstatus(status){
    document.getElementById("status").value = status
  }
  eel.expose(getInput);
  function getInput(input){
    var input = document.getElementById("textin");
    return input.value;
  }
  eel.expose(setOutput);
  function setOutput(output){
    document.getElementById("textout").value = output

  }

  function add()
      {
          var textin = document.getElementById("textin").value;
          var textout = document.getElementById("textout").value;
          var status = document.getElementById("status").value;
          var searchin = document.getElementById("searchin").value;
          var parameters = document.getElementById("parameters").value;
          var proxy = document.getElementById("proxyList").value

          if(textin.length > 0){
            localStorage.setItem("textin", textin);
          }
          else{
            localStorage.setItem("textin", "");
          }

          if(textout.length > 0){
            localStorage.setItem("textout", textout);
          }
          else{
            localStorage.setItem("textout", "");
          }

          if(status.length > 0){
            localStorage.setItem("status", status);
          }
          else{
            localStorage.setItem("status", "");
          }

          if(searchin.length > 0){
            localStorage.setItem("searchin", searchin);
          }
          else{
            localStorage.setItem("searchin", "");
          }
          if(parameters.length > 0){
            localStorage.setItem("parameters", parameters);
          }
          else{
            localStorage.setItem("parameters", "");
          }
          if(proxy.length > 0){
            localStorage.setItem("proxy", proxy);
          }
          else{
            localStorage.setItem("proxy", "");
          }
      }


  window.onload = function load() {
      document.getElementById("textin").value = localStorage.getItem("textin");
      document.getElementById("textout").value = localStorage.getItem("textout");
      document.getElementById("status").value = sessionStorage.getItem("status");
      document.getElementById("searchin").value = localStorage.getItem("searchin");
      document.getElementById("parameters").value = localStorage.getItem("parameters");
      document.getElementById("proxyList").value = localStorage.getItem("proxy");

  };
  eel.expose(find);
  function find() {
    eel.py_find()
  }
  eel.expose(getKeyWord);
  function getKeyWord(){
    var keyWord = document.getElementById("searchin");
    return keyWord.value;
  }
  eel.expose(findSetOutput);
  function findSetOutput(value){
    document.getElementById("textout").value = value;
    document.getElementById("status").value = "Results Found";
  }
  eel.expose(setOutput);
  function setOutput(value){
    document.getElementById("textout").value = value;
  }
  eel.expose(proxy_status);
  function proxy_status(){
    
    var proxy_status = $('#proxy').is(':checked'); 
    
    return proxy_status;
    
  }
  eel.expose(proxy_list);
  function proxy_list(){
    var data = localStorage.getItem("proxyList");
    return data

  }
  eel.expose(fallback_status);
  function fallback_status(){
    var data = localStorage.getItem("fallback_status");
    return data

  }
  eel.expose(parameters);
  function parameters(){
    var data = localStorage.getItem("parameters");
    return data

  }

  function getPathToFilePython(){
    eel.getPathToFile()
  }

  eel.expose(setDataFromFile)
  function setDataFromFile(data){
    document.getElementById("textin").value = data
  }
