<template>
    <div class="events-page">
      <div class="events-container">
        <h1 class="events-title">Upcoming Campus Events</h1>
  
        <div class="events-list">
          <div v-for="event in events" :key="event.id" class="event-card">
            <h2 class="event-name">{{ event.name }}</h2>
            <p class="event-info">
              📅 {{ event.date }} — 📍 {{ event.location }}
            </p>
            <p class="event-description">{{ event.description }}</p>
          </div>
        </div>
  
        <div class="map-placeholder">
          <iframe
            width="1000"
            height="300"
            style="border:0"
            loading="lazy"
            allowfullscreen
            referrerpolicy="no-referrer-when-downgrade"
            src="https://www.google.com/maps/embed/v1/place?key=YOUR_API_KEY&q=Purdue+Northwest+University"> <!-- Need API key to test -->
          </iframe>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const events = ref([
    {
      id: 1,
      name: 'Intramural Cricket',
      date: 'April 27, 2025, 11:00 AM - 1:00 PM',
      location: 'PNW Campus Field',
      description: 'Gather your friends and join Intramural Cricket!',
    },
    {
      id: 2,
      name: 'Intramural Fishing Challenge',
      date: 'April 28, 2025',
      location: 'PNW Campus Lake',
      description: 'Get ready to tackle the competition in our Fishing Challenge!',
    },
    {
      id: 3,
      name: 'Study Away 101: Students’ Guide to Going Global',
      date: 'April 28, 2025, 12:00 PM - 1:00 PM',
      location: 'Study Abroad Office',
      description: 'Prepare to expand your global horizons at our Study Away session.',
    },
    {
      id: 4,
      name: 'Pancake Study Break (Westville)',
      date: 'April 28, 2025, 12:00 PM - 2:00 PM',
      location: 'Westville Campus',
      description: 'Take a break from studying and come have some fun with pancakes!',
    },
    {
      id: 5,
      name: 'CHESS Day of Giving Party!',
      date: 'April 30, 2025, 1:00 PM - 2:30 PM',
      location: 'CHESS Building Lawn',
      description: 'Celebrate the College of Humanities, Education, and Social Sciences!',
    }
  ])
  </script>
  
  <style scoped>
  .events-page {
    min-height: 100vh;
    padding: 2rem;
    background: linear-gradient(to bottom, var(--pnw-white), #f3f4f6);
  }
  
  .events-container {
    max-width: 1000px;
    margin: 0 auto;
  }
  
  .events-title {
    font-size: 2.5rem;
    font-weight: bold;
    color: var(--pnw-gold); /* Purdue Northwest Gold */
    text-align: center;
    margin-bottom: 2rem;
  }
  
  .events-list {
    display: grid;
    gap: 2rem;
  }
  
  .event-card {
    background-color: var(--pnw-white);
    border: 1px solid #ccc;
    border-radius: 0.75rem;
    padding: 1.5rem;
    transition: transform 0.3s, box-shadow 0.3s;
  }
  
  .event-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }
  
  .event-name {
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--pnw-black);
    margin-bottom: 0.5rem;
  }
  
  .event-info {
    font-size: 0.9rem;
    color: var(--pnw-gray);
    margin-bottom: 1rem;
  }
  
  .event-description {
    color: #444444;
    font-size: 1rem;
  }
  
  .map-placeholder {
    background-color: #e5e7eb;
    border-radius: 0.75rem;
    height: 300px;
    margin-top: 3rem;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #555555;
    font-size: 1.2rem;
    font-style: italic;
  }
  </style>
  