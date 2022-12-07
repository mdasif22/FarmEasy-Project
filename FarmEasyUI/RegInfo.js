// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBTAQ7ispF6N0VROEL9Z38wP2PDytj764k",
  authDomain: "farmer-user-project.firebaseapp.com",
  databaseURL: "https://farmer-user-project-default-rtdb.firebaseio.com",
  projectId: "farmer-user-project",
  storageBucket: "farmer-user-project.appspot.com",
  messagingSenderId: "509647514702",
  appId: "1:509647514702:web:d337daa1754c417e84271f"
};

  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  // Initialize variables
  const auth = firebase.auth()
  const database = firebase.database()
  
  // Set up our register function
  function regasfarmer () {
    // Get all our input fields
    full_name = document.getElementById('name').value
    email = document.getElementById('email').value
    password = document.getElementById('password').value
    mobile = document.getElementById('mobile').value
    gender = document.getElementById('gender').value
    dob = document.getElementById('dob').value
    address = document.getElementById('address').value
    city = document.getElementById('city').value
    pin = document.getElementById('pin').value
    state = document.getElementById('state').value

    // Validate input fields
    if (validate_email(email) == false || validate_password(password) == false) {
      alert('Please Enter a Proper Email or Password')
      return
      // Don't continue running the code
    }
    // if (validate_field(full_name) == false || validate_field(phone) == false) {
    //   alert('One or More Extra Fields is Outta Line!!')
    //   return
    // }
   
    // Move on with Auth
    auth.createUserWithEmailAndPassword(email, password)
    .then(function() {
      // Declare user variable
      var user = auth.currentUser
  
      // Add this user to Firebase Database
      var database_ref = database.ref()
  
      // Create User data
      var user_data = {
        email : email,
        password : password,
        full_name : full_name,
        mobile : mobile,
        address : address,
        full_name : full_name,
        email : email,
        password : password,
        mobile : mobile,
        gender : gender,
        dob : dob,
        address : address,
        city : city,
        pin : pin,
        state : state,
        last_login : Date.now()
      }
  
      // Push to Firebase Database
      database_ref.child('farmer/' + user.uid).set(user_data)
  
      // Done
      alert('Farmer Created!!')
    })
    .catch(function(error) {
      // Firebase will use this to alert of its errors
      var error_code = error.code
      var error_message = error.message
  
      alert(error_message)
    })
  }
  
//Buyer registration 
function regasbuyer () {
  // Get all our input fields
  full_name = document.getElementById('name').value
  email = document.getElementById('email').value
  password = document.getElementById('password').value
  mobile = document.getElementById('mobile').value
  gender = document.getElementById('gender').value
  dob = document.getElementById('dob').value
  address = document.getElementById('address').value
  city = document.getElementById('city').value
  pin = document.getElementById('pin').value
  state = document.getElementById('state').value

  // Validate input fields
  if (validate_email(email) == false || validate_password(password) == false) {
    alert('Please Enter a Proper Email or Password')
    return
    // Don't continue running the code
  }
  // if (validate_field(full_name) == false || validate_field(phone) == false) {
  //   alert('One or More Extra Fields is Outta Line!!')
  //   return
  // }
 
  // Move on with Auth
  auth.createUserWithEmailAndPassword(email, password)
  .then(function() {
    // Declare user variable
    var user = auth.currentUser

    // Add this user to Firebase Database
    var database_ref = database.ref()

    // Create User data
    var user_data = {
      email : email,
      password : password,
      full_name : full_name,
      mobile : mobile,
      address : address,
      full_name : full_name,
      email : email,
      password : password,
      mobile : mobile,
      gender : gender,
      dob : dob,
      address : address,
      city : city,
      pin : pin,
      state : state,
      last_login : Date.now()
    }

    // Push to Firebase Database
    database_ref.child('buyer/' + user.uid).set(user_data)

    // Done
    alert('Buyer Created!!')
  })
  .catch(function(error) {
    // Firebase will use this to alert of its errors
    var error_code = error.code
    var error_message = error.message

    alert(error_message)
  })
}

  //Set up our login function
  function login () {
    // Get all our input fields
    email = document.getElementById('email').value
    password = document.getElementById('password').value
  
    // Validate input fields
    if (validate_email(email) == false || validate_password(password) == false) {
      alert('Email or Password is Outta Line!!')
      return
      // Don't continue running the code
    }
  
    auth.signInWithEmailAndPassword(email, password)
    .then(function() {
      // Declare user variable
      var user = auth.currentUser
  
      // Add this user to Firebase Database
      var database_ref = database.ref()
  
      // Create User data
      var user_data = {
        last_login : Date.now()
      }
  
      // Push to Firebase Database
      database_ref.child('users/' + user.uid).update(user_data)
  
      // DOne
      alert('User Logged In!!')
  
    })
    .catch(function(error) {
      // Firebase will use this to alert of its errors
      var error_code = error.code
      var error_message = error.message
  
      alert(error_message)
    })
  }
  
  
  
  
  // Validate Functions
  function validate_email(email) {
    expression = /^[^@]+@\w+(\.\w+)+\w$/
    if (expression.test(email) == true) {
      // Email is good
      return true
    } else {
      // Email is not good
      return false
    }
  }
  
  function validate_password(password) {
    // Firebase only accepts lengths greater than 6
    if (password < 6) {
      return false
    } else {
      return true
    }
  }
  
  function validate_field(field) {
    if (field == null) {
      return false
    }
  
    if (field.length <= 0) {
      return false
    } else {
      return true
    }
  }