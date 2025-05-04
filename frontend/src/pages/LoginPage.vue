<template>
  <div class="login-page">
    <div class="login-form">
      <h1 class="page-title">Login</h1>
      <form @submit.prevent="handleSubmit" class="form">
        <div class="form-group">
          <label for="email">Email:</label>
          <input id="email" v-model="email" type="email" required />
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input id="password" v-model="password" type="password" required />
        </div>
        <button type="submit" class="btn">Login</button>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </form>
      <p class="signup-prompt">
        Don't have an account? <router-link to="/register">Please sign up</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { inject } from 'vue'

const email = ref('')
const password = ref('')
const errorMessage = ref('')
const router = useRouter()
const auth = inject('auth')

const handleSubmit = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        email: email.value,
        password: password.value
      })
    });

    const data = await response.json();

    if (response.ok) {
      auth.login(data)
      router.push('/profile')
    } else {
      errorMessage.value = data.error || 'Login failed'
    }
  } catch (error) {
    console.error('Login error:', error)
    errorMessage.value = 'An error occurred during login'
  }
}
</script>

<style scoped>
.login-page /* Laz: Added a new div and changes the OG login page to login-form, that way you can edit the background as well. */ {
  min-height: 100vh;
  background: linear-gradient(to bottom, var(--pnw-white), #f3f4f6);
  justify-content: center;
  align-items: center;
  padding: 2rem;
}

.login-form {
  max-width: 400px;
  border: 2px solid var(--pnw-gold);
  margin: 2rem auto;
  padding: 2rem;
  background: var(--pnw-white);
  border-radius: 0.75rem;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
}

.page-title {
  font-size: 2rem;
  color: var(--pnw-gold);
  text-align: center;
  margin-bottom: 1.5rem;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: var(--pnw-black);
}

input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.375rem;
}

.btn {
  width: 100%;
  padding: 0.75rem;
  background-color: var(--pnw-gold);
  color: var(--pnw-black);
  font-weight: 700;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn:hover {
  background-color: #bfa32f;
}

.error-message {
  color: #ff4444;
  margin-top: 1rem;
  text-align: center;
}
</style>
