<template>
  <div class="register-event-page">
    <div class="register-event-form">
      <h1 class="page-title">Add New Event</h1>
      <form @submit.prevent="handleRegister" class="form">
        <div class="form-group">
          <label for="eventName">Event Name:</label>
          <input id="eventName" v-model="formData.event_name" type="text" required />
        </div>
        
        <div class="form-group">
          <label for="abstract">Event Description:</label>
          <textarea id="abstract" v-model="formData.abstract" required></textarea>
        </div>

        <div class="form-group">
          <label for="date">Event Date and Time:</label>
          <input id="date" v-model="formData.date" type="datetime-local" required />
        </div>

        <div class="form-group">
          <label for="cost">Event Cost ($):</label>
          <input id="cost" v-model="formData.cost" type="number" min="0" step="0.01" />
        </div>

        <div class="form-group">
          <label for="street_address">Street Address:</label>
          <input id="street_address" v-model="formData.street_address" type="text" required />
        </div>

        <div class="form-row">
          <div class="form-group">
            <label for="city">City:</label>
            <input id="city" v-model="formData.city" type="text" required />
          </div>

          <div class="form-group">
            <label for="state">State:</label>
            <input id="state" v-model="formData.state" type="text" required />
          </div>

          <div class="form-group">
            <label for="zip_code">ZIP Code:</label>
            <input id="zip_code" v-model="formData.zip_code" type="text" required />
          </div>
        </div>

        <div v-if="error" class="error-message">
          {{ error }}
        </div>

        <button type="submit" class="btn" :disabled="loading">
          {{ loading ? 'Adding Event...' : 'Add Event' }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const loading = ref(false)
const error = ref(null)

const formData = ref({
  event_name: '',
  abstract: '',
  date: '',
  cost: 0,
  street_address: '',
  city: '',
  state: '',
  zip_code: ''
})

const handleRegister = async () => {
  try {
    loading.value = true
    error.value = null

    // Format the date to YYYY-MM-DD
    const date = new Date(formData.value.date)
    const formattedDate = date.toISOString().split('T')[0]

    const formattedData = {
      ...formData.value,
      date: formattedDate
    }

    console.log('Submitting data:', formattedData)

    const response = await fetch('http://localhost:8000/api/events/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formattedData)
    })

    if (!response.ok) {
      const data = await response.json()
      console.error('Error response:', data)
      
      // Show user-friendly error message
      if (data.message && data.message.includes('address')) {
        throw new Error('Please enter a valid address')
      } else if (data.date) {
        throw new Error('Please enter a valid date')
      } else {
        throw new Error('Failed to add event. Please check your input and try again.')
      }
    }

    // Clear the form
    formData.value = {
      event_name: '',
      abstract: '',
      date: '',
      cost: 0,
      street_address: '',
      city: '',
      state: '',
      zip_code: ''
    }

    // Redirect to events page
    router.push('/events')
  } catch (err) {
    error.value = err.message
    console.error('Error adding event:', err)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.register-event-page {
  min-height: 100vh;
  background: linear-gradient(to bottom, var(--pnw-white), #f3f4f6);
  padding: 2rem;
}

.register-event-form {
  max-width: 600px;
  margin: 2rem auto;
  border: 2px solid var(--pnw-gold);
  padding: 2rem;
  background: var(--pnw-white);
  border-radius: 0.75rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
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

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1rem;
}

label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: var(--pnw-black);
}

input, textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.375rem;
}

textarea {
  min-height: 100px;
  resize: vertical;
}

.error-message {
  color: #dc3545;
  margin-bottom: 1rem;
  padding: 0.5rem;
  background-color: #f8d7da;
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

.btn:hover:not(:disabled) {
  background-color: #bfa32f;
}

.btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}
</style>
