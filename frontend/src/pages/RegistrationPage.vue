<template>
  <div class="registration-page">
    <div class="form-container">
      <h1>Create Account</h1>

      <div v-if="isRegistrationEnabled">
        <form @submit.prevent="handleSubmit">
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" v-model="form.email" required />
          </div>

          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" v-model="form.password" required />
          </div>

          <div class="form-group">
            <label for="fname">First Name</label>
            <input type="text" id="fname" v-model="form.fname" required />
          </div>

          <div class="form-group">
            <label for="mname">Middle Name</label>
            <input type="text" id="mname" v-model="form.mname" />
          </div>

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

          <button type="submit" class="submit-button">Create Account</button>
        </form>
      </div>

      <div v-else class="error-message">
        <h2>Registration is currently disabled.</h2>
        <p>Please try again later.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const isRegistrationEnabled = ref(true)

const form = ref({
  email: '',
  password: '',
  fname: '',
  mname: '',
  lname: '',
  street_address: '',
  city: '',
  state: '',
  zip_code: '',
})

const handleSubmit = async () => {
  try {
    console.log('Submitting form:', form.value)
    const response = await fetch('http://localhost:8000/api/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify(form.value),
    })

    console.log('Response status:', response.status)
    const responseText = await response.text()
    console.log('Response text:', responseText)
    
    let data
    try {
      data = JSON.parse(responseText)
    } catch (e) {
      console.error('Failed to parse JSON:', e)
      throw new Error('Server returned invalid JSON response')
    }
    
    if (response.ok) {
      alert('Account created successfully!')
      router.push('/login')
    } else {
      // Show more detailed error message
      const errorMessage = Object.entries(data)
        .map(([key, value]) => `${key}: ${value}`)
        .join('\n')
      alert(`Registration failed:\n${errorMessage}`)
    }
  } catch (error) {
    console.error('Registration error:', error)
    alert(`An error occurred during registration: ${error.message}`)
  }
}
</script>

<style scoped>
.registration-page {
  min-height: 100vh;
  background: linear-gradient(to bottom, var(--pnw-white), #f3f4f6);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0rem;
}

.form-container {
  background-color: var(--pnw-white);
  border: 2px solid var(--pnw-gold);
  border-radius: 12px;
  padding: 2rem;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
}

h1 {
  color: var(--pnw-gold);
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
  border: 1px solid #ccc;
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
  background-color: #bfa32f;
}

.error-message {
  text-align: center;
  color: var(--pnw-black);
}

.error-message h2 {
  color: var(--pnw-gold);
}
</style>
