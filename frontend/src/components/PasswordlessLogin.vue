<template>
  <div>
    <Button 
      label="Sign in with Email" 
      icon="pi pi-envelope" 
      @click="visible = true"
      severity="secondary"
    />
    
    <Dialog v-model:visible="visible" modal :header="step === 'email' ? 'Sign in with Email' : 'Enter Code'" :style="{ width: '25rem' }">
      <!-- Step 1: Enter Email -->
      <form v-if="step === 'email'" @submit.prevent="handleSendCode" class="flex flex-col gap-4">
        <p class="text-sm text-gray-600">We'll send you a magic link and a code to sign in.</p>
        
        <div class="flex flex-col gap-2">
          <label for="email" class="font-semibold">Email</label>
          <InputText 
            id="email" 
            v-model="email" 
            type="email" 
            required 
            placeholder="Enter your email"
            :disabled="loading"
          />
        </div>

        <Message v-if="error" severity="error" :closable="false">{{ error }}</Message>
        
        <div class="flex justify-end gap-2 mt-4">
          <Button type="button" label="Cancel" severity="secondary" @click="visible = false" :disabled="loading" />
          <Button type="submit" label="Send Code" icon="pi pi-send" :loading="loading" />
        </div>
      </form>

      <!-- Step 2: Enter Code -->
      <form v-else-if="step === 'code'" @submit.prevent="handleVerifyCode" class="flex flex-col gap-4">
        <p class="text-sm text-gray-600">
          We sent a code to <strong>{{ email }}</strong>. 
          Check your email for the code or click the magic link.
        </p>
        
        <div class="flex flex-col gap-2">
          <label for="code" class="font-semibold">Enter Code</label>
          <InputText 
            id="code" 
            v-model="code" 
            type="text" 
            required 
            placeholder="Enter 6-digit code"
            :disabled="loading"
            maxlength="6"
          />
        </div>

        <Message v-if="error" severity="error" :closable="false">{{ error }}</Message>
        <Message v-if="successMessage" severity="success" :closable="false">{{ successMessage }}</Message>
        
        <div class="flex justify-between items-center mt-4">
          <Button 
            type="button" 
            label="Resend Code" 
            severity="secondary" 
            text
            @click="handleResendCode" 
            :disabled="loading || resendDisabled"
          />
          <Button type="submit" label="Verify" icon="pi pi-check" :loading="loading" />
        </div>
      </form>
    </Dialog>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { createPasswordlessCode, consumePasswordlessCode, resendPasswordlessCode } from '../auth';
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
    const step = ref('email'); // 'email' or 'code'
    const email = ref('');
    const code = ref('');
    const loading = ref(false);
    const error = ref('');
    const successMessage = ref('');
    const resendDisabled = ref(false);

    const handleSendCode = async () => {
      loading.value = true;
      error.value = '';
      
      try {
        const result = await createPasswordlessCode(email.value);
        
        if (result.status === 'OK') {
          step.value = 'code';
          successMessage.value = 'Code sent! Check your email.';
        } else {
          error.value = 'Failed to send code. Please try again.';
        }
      } catch (e) {
        error.value = 'An error occurred. Please try again.';
        console.error('Send code error:', e);
      } finally {
        loading.value = false;
      }
    };

    const handleVerifyCode = async () => {
      loading.value = true;
      error.value = '';
      successMessage.value = '';
      
      try {
        const result = await consumePasswordlessCode(code.value);
        
        if (result.status === 'OK') {
          // Check if this is a new user and register if needed
          const createdNewUser = result.createdNewRecipeUser;
          
          if (createdNewUser) {
            try {
              const apiDomain = import.meta.env.VITE_API_DOMAIN || 'http://localhost:8123';
              await fetch(`${apiDomain}/api/v1/user/register`, {
                method: 'PUT',
                credentials: 'include',
                headers: {
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email: email.value })
              });
            } catch (registerErr) {
              console.error('Registration error:', registerErr);
            }
          }
          
          // Close dialog and redirect
          visible.value = false;
          router.push('/');
        } else if (result.status === 'INCORRECT_USER_INPUT_CODE_ERROR') {
          error.value = 'Invalid code. Please try again.';
        } else if (result.status === 'EXPIRED_USER_INPUT_CODE_ERROR') {
          error.value = 'Code expired. Please request a new one.';
        } else {
          error.value = 'Verification failed. Please try again.';
        }
      } catch (e) {
        error.value = 'An error occurred. Please try again.';
        console.error('Verify code error:', e);
      } finally {
        loading.value = false;
      }
    };

    const handleResendCode = async () => {
      loading.value = true;
      error.value = '';
      successMessage.value = '';
      resendDisabled.value = true;
      
      try {
        const result = await resendPasswordlessCode();
        
        if (result.status === 'OK') {
          successMessage.value = 'Code resent! Check your email.';
          
          // Disable resend button for 30 seconds
          setTimeout(() => {
            resendDisabled.value = false;
          }, 30000);
        } else {
          error.value = 'Failed to resend code.';
          resendDisabled.value = false;
        }
      } catch (e) {
        error.value = 'An error occurred.';
        resendDisabled.value = false;
        console.error('Resend code error:', e);
      } finally {
        loading.value = false;
      }
    };

    return {
      visible,
      step,
      email,
      code,
      loading,
      error,
      successMessage,
      resendDisabled,
      handleSendCode,
      handleVerifyCode,
      handleResendCode
    };
  }
};
</script>
