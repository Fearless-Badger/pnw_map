<template>
    <div class="registration-page">
      <div class="form-container">
        <h1>Student Registration</h1>
  
        <div v-if="isRegistrationEnabled">
          <form @submit.prevent="handleSubmit">
            <div class="form-group">
              <label for="fname">First Name</label>
              <input type="text" id="fname" v-model="form.fname" required />
            </div>
  
            <div class="form-group">
              <label for="mname">Middle Name</label>
              <input type="text" id="mname" v-model="form.mname" />
            </div> 
<!-- Laz: mname Not required, hopefully as intended. I don't even have a middle name. -->
  
            <div class="form-group">
              <label for="lname">Last Name</label>
              <input type="text" id="lname" v-model="form.lname" required />
            </div>
  
            <div class="form-group">
              <label for="street_address">Street Address</label>
              <input type="text" id="street_address" v-model="form.street_address" required />
            </div>
  
            <div class="form-group">
              <label for="city">City</label>
              <input type="text" id="city" v-model="form.city" required />
            </div>
  
            <div class="form-group">
              <label for="state">State</label>
              <input type="text" id="state" v-model="form.state" required />
            </div>
  
            <div class="form-group">
              <label for="zip_code">Zip Code</label>
              <input type="text" id="zip_code" v-model="form.zip_code" required />
            </div>
  
            <button type="submit" class="submit-button">Register</button>
          </form>
        </div>
        
        <div v-else class="error-message">
          <h2>Registration is currently disabled.</h2>
          <p>Please try again later.</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "RegistrationPage",
    data() {
      return {
        isRegistrationEnabled: true, // boolean to control if worked or not for testing (For: Micah/Backend)
        form: {
          fname: "",
          mname: "",
          lname: "",
          street_address: "",
          city: "",
          state: "",
          zip_code: "",
        }
      };
    },
    methods: {
      handleSubmit() {
        console.log("Registering student:", this.form);
        alert("Registration successful!");
        
        this.form = {
          fname: "",
          mname: "",
          lname: "",
          street_address: "",
          city: "",
          state: "",
          zip_code: "",
        };
      }
    }
  };
  </script>
  
  <style scoped>
    .registration-page {
    min-height: 100vh;
    background: linear-gradient(to bottom, var(--pnw-white), #f3f4f6);
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 2rem;
  }
  
  .form-container {
    background-color: var(--pnw-white);
    border: 2px solid var(--pnw-gold);
    border-radius: 8px;
    padding: 2rem;
    width: 100%;
    max-width: 500px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  h1 {
    color: var(--pnw-black);
    text-align: center;
    margin-bottom: 1.5rem;
  }
  
  .form-group {
    margin-bottom: 1rem;
  }
  
  label {
    display: block;
    margin-bottom: 0.5rem;
    color: var(--pnw-black);
    font-weight: bold;
  }
  
  input {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid var(--pnw-campus-gold);
    border-radius: 4px;
  }
  
  .submit-button {
    width: 100%;
    padding: 0.75rem;
    background-color: var(--pnw-gold);
    color: var(--pnw-black);
    font-weight: bold;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background 0.3s ease;
  }
  
  .submit-button:hover {
    background-color: #bfa32f;;
  }
  
  .error-message {
    text-align: center;
    color: var(--pnw-black);
  }
  
  .error-message h2 {
    color: var(--pnw-gold);
  }
  </style>
  