// Initialize Firebase (ADD YOUR OWN DATA)
const firebaseConfig = {
    apiKey: "AIzaSyBTAQ7ispF6N0VROEL9Z38wP2PDytj764k",
    authDomain: "farmer-user-project.firebaseapp.com",
    databaseURL: "https://farmer-user-project-default-rtdb.firebaseio.com",
    projectId: "farmer-user-project",
    storageBucket: "farmer-user-project.appspot.com",
    messagingSenderId: "509647514702",
    appId: "1:509647514702:web:d337daa1754c417e84271f"
  };
  
  firebase.initializeApp(firebaseConfig);
  
  // Reference messages collection
  var messagesRef = firebase.database().ref();
  
  // Listen for form submit
  document.getElementById('crop').addEventListener('submit', submitForm);
  
  // Submit form
  function submitForm(e){
    e.preventDefault();
  
    // Get values
    var wheat = getInputVal('wheat');
    var wheat_price = getInputVal('wprice');
    var rice = getInputVal('rice');
    var rice_price = getInputVal('rprice');
    var pulse = getInputVal('pulse');
    var pulse_price = getInputVal('pprice');
    var spice = getInputVal('spice');
    var spice_price = getInputVal('sprice');
    var vegetable = getInputVal('veg');
    var veg_price = getInputVal('vprice');
  
    // Save message
    saveMessage(wheat, wheat_price, rice, rice_price, pulse,pulse_price,spice,spice_price,vegetable,veg_price);
  
    // Show alert
    document.querySelector('.alert').style.display = 'block';
  
    // Hide alert after 3 seconds
    setTimeout(function(){
      document.querySelector('.alert').style.display = 'none';
    },3000);
  
    // Clear form
    document.getElementById('crop').reset();
  }
  
  // Function to get get form values
  function getInputVal(id){
    return document.getElementById(id).value;
  }
  
  // Save message to firebase
  function saveMessage(wheat, wheat_price, rice, rice_price, pulse,pulse_price,spice,spice_price,vegetable,veg_price){
    var user = auth.currentUser
    var newMessageRef = messagesRef.child("farmer/"+ user.id).push();
    newMessageRef.set({
         wheat: wheat,
         wheat_price : wheat_price,
         rice : rice,
         rice_price : rice_price,
         pulse : pulse,
         pulse_price : pulse_price,
         spice : spice,
         spice_price : spice_price,
         vegetable : vegetable,
         veg_price : veg_price,
    });
  }