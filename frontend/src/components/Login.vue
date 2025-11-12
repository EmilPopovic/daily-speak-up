<template>
  <div>
    <Button @click="handleLogin" label="Log in" />
  </div>
</template>
<script setup>
  import { useAuth0 } from '@auth0/auth0-vue';
  import Button from 'primevue/button'; 

  const { loginWithRedirect } = useAuth0();

  const handleLogin = () => {
    loginWithRedirect();
  };
</script>
