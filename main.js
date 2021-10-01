

const electron = require('electron')
const app = electron.app
const BrowserWindow = electron.BrowserWindow


let mainWindow


function createWindow () {
  
  var mainWindow = new BrowserWindow({
    backgroundColor: '#FFFFFF',
    show: false,
    maximizable: false,
    minWidth: 500,
    minHeight: 515,
    autoHideMenuBar: true,
    center: true,
    icon:'web/img/logo2white.jpg',
    // webPreferences: {
    //   devTools: false
    // }
    


  });

  mainWindow.once('ready-to-show', () => {
    mainWindow.show()
  })


 
  mainWindow.loadURL('http://localhost:1904/home.html');
  mainWindow.setMenuBarVisibility(false)
  
  mainWindow.on('closed', function () {
    mainWindow = null
  })
}


app.on('ready', createWindow)

app.on('window-all-closed', function () {
  app.quit()
});

app.on('activate', function () {
  if (mainWindow === null) {
    createWindow()
  }
})

