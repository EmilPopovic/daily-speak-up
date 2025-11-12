<template>
  <div>
    <Button label="Sign up" icon="pi pi-user-plus" severity="secondary" @click="visible = true" />
    
    <Dialog v-model:visible="visible" modal header="Sign up" :style="{ width: '25rem' }">
      <form @submit.prevent="handleSignup" class="flex flex-col gap-4">
        <div class="flex flex-col gap-2">
          <label for="signup-email" class="font-semibold">Email</label>
          <InputText 
            id="signup-email" 
            v-model="email" 
            type="email" 
            required 
            placeholder="Enter your email"
            :disabled="loading"
          />
        </div>
        
        <div class="flex flex-col gap-2">
          <label for="signup-password" class="font-semibold">Password</label>
          <InputText 
            id="signup-password" 
            v-model="password" 
            type="password" 
            required 
            placeholder="Enter your password"
            :disabled="loading"
          />
        </div>

        <Message v-if="error" severity="error" :closable="false">{{ error }}</Message>
        <Message v-if="success" severity="success" :closable="false">{{ success }}</Message>
        
        <div class="flex justify-end gap-2 mt-4">
          <Button type="button" label="Cancel" severity="secondary" @click="visible = false" :disabled="loading" />
          <Button type="submit" label="Sign up" icon="pi pi-user-plus" :loading="loading" />
        </div>
      </form>
    </Dialog>
  </div>
</template>

<script>
import { ref } from 'vue';
import { signUp } from '../auth';
import { useRouter } from 'vue-router';
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';
import InputText from 'primevue/inputtext';
import Message from 'primevue/message';

export default {
  components: {
    Button,
    Dialog,
    InputText,
    Message
  },
  setup() {
    const router = useRouter();
    const visible = ref(false);
    const email = ref('');
    const password = ref('');
    const loading = ref(false);
    const error = ref('');
    const success = ref('');

    const handleSignup = async () => {
      loading.value = true;
      error.value = '';
      success.value = '';
      
      try {
        const result = await signUp(email.value, password.value);
        
        if (result.status === 'OK') {
          success.value = 'Account created successfully! Redirecting...';
          setTimeout(() => {
            visible.value = false;
            email.value = '';
            password.value = '';
            router.push('/');
          }, 1500);
        } else if (result.status === 'FIELD_ERROR') {
          error.value = result.formFields.map(f => f.error).join(', ');
        } else if (result.status === 'EMAIL_ALREADY_EXISTS_ERROR') {
          error.value = 'This email is already registered. Please login instead.';
        }
      } catch (e) {
        error.value = 'An error occurred during signup. Please try again.';
        console.error('Signup error:', e);
      } finally {
        loading.value = false;
      }
    };

    return {
      visible,
      email,
      password,
      loading,
      error,
      success,
      handleSignup
    };
  }
};
</script>
