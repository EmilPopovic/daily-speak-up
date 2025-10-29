<template>
  <div v-if="user">
    <img :src="user.picture" alt="Profile Picture" />
    <h2>{{ user.name }}</h2>
    <p>{{ user.email }}</p>
  </div>
</template>

<script>
import { useAuth0 } from '@auth0/auth0-vue';

export default {
  setup() {
    const { user } = useAuth0();
    console.log(user);
    return { user };
  },
};
</script>
