<template>
  <div>
    <button 
      @click="showModal = true"
      class="px-6 py-2.5 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition-all duration-200 shadow-sm hover:shadow-md"
    >
      Log In
    </button>

    <Transition name="modal">
      <div 
        v-if="showModal" 
        class="fixed inset-0 flex items-center justify-center z-50 p-4"
        @click.self="closeModal"
      >
        <div class="bg-white rounded-2xl shadow-2xl w-full max-w-md relative">
          <button 
            @click="closeModal"
            class="absolute top-4 right-4 text-gray-400 hover:text-gray-800 transition-colors"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>

          <div class="text-center pt-8 pb-6 px-8 border-b border-gray-100">
            <div class="w-16 h-16 bg-blue-600 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
            </div>
            <h2 class="text-2xl font-bold text-gray-800">Welcome Back</h2>
            <p class="text-gray-500 mt-2">Sign in to continue to DailySpeakUp</p>
          </div>

          <div class="p-8">
            <button
              @click="handleGoogleLogin"
              class="w-full flex items-center justify-center gap-3 px-4 py-3 bg-white border-2 border-gray-300 rounded-lg hover:bg-gray-50 transition-colors font-medium text-gray-700 hover:border-gray-400 mb-4"
            >
              <svg class="w-5 h-5" viewBox="0 0 24 24">
                <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
              </svg>
              Continue with Google
            </button>

            <div class="relative my-6">
              <div class="absolute inset-0 flex items-center">
                <div class="w-full border-t border-gray-300"></div>
              </div>
              <div class="relative flex justify-center text-sm">
                <span class="px-4 bg-white text-gray-500 font-medium">OR</span>
              </div>
            </div>

            <div v-if="!showCodeInput">
              <label class="block text-sm font-medium text-gray-700 mb-2">Email address</label>
              <input
                v-model="email"
                type="email"
                placeholder="you@example.com"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all outline-none"
                @keyup.enter="handleEmailLogin"
              />
              <button
                @click="handleEmailLogin"
                :disabled="!email || emailLoading"
                class="w-full mt-4 px-4 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition-colors disabled:bg-gray-300 disabled:cursor-not-allowed flex items-center justify-center"
              >
                <span v-if="emailLoading" class="flex items-center gap-2">
                  <svg class="animate-spin h-5 w-5" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  <span>Sending...</span>
                </span>
                <span v-else>Continue</span>
              </button>
            </div>

            <div v-else>
              <button 
                @click="showCodeInput = false" 
                class="flex items-center gap-2 text-sm text-gray-600 hover:text-gray-800 mb-4"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                </svg>
                Back
              </button>
              
              <div class="mb-4 p-4 bg-blue-50 rounded-lg border border-blue-100">
                <p class="text-sm text-blue-800">
                  We've sent a verification code to <strong>{{ email }}</strong>
                </p>
              </div>

              <label class="block text-sm font-medium text-gray-700 mb-2">Verification Code</label>
              <input
                v-model="code"
                type="text"
                placeholder="Enter 6-digit code"
                maxlength="6"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all outline-none text-center text-2xl tracking-widest font-mono"
                @keyup.enter="handleCodeVerification"
              />
              
              <button
                @click="handleCodeVerification"
                :disabled="code.length !== 6 || codeLoading"
                class="w-full mt-4 px-4 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition-colors disabled:bg-gray-300 disabled:cursor-not-allowed flex items-center justify-center"
              >
                <span v-if="codeLoading" class="flex items-center gap-2">
                  <svg class="animate-spin h-5 w-5" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  <span>Verifying...</span>
                </span>
                <span v-else>Verify</span>
              </button>

              <div class="mt-4 text-center">
                <button
                  @click="handleResendCode"
                  :disabled="resendCooldown > 0"
                  class="text-sm text-blue-600 hover:text-blue-700 disabled:text-gray-400 disabled:cursor-not-allowed"
                >
                  {{ resendCooldown > 0 ? `Resend code in ${resendCooldown}s` : 'Resend code' }}
                </button>
              </div>
            </div>

            <div v-if="errorMessage" class="mt-4 p-3 bg-red-50 border border-red-200 rounded-lg">
              <p class="text-sm text-red-800">{{ errorMessage }}</p>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import { signInWithGoogle, createPasswordlessCode, consumePasswordlessCode, resendPasswordlessCode } from '../auth';
import { useRouter } from 'vue-router';

const router = useRouter();
const showModal = ref(false);
const email = ref('');
const code = ref('');
const showCodeInput = ref(false);
const emailLoading = ref(false);
const codeLoading = ref(false);
const errorMessage = ref('');
const resendCooldown = ref(0);

const handleEscapeKey = (event: KeyboardEvent) => {
  if (event.key === 'Escape' && showModal.value) {
    closeModal();
  }
};

onMounted(() => {
  document.addEventListener('keydown', handleEscapeKey);
});

onUnmounted(() => {
  document.removeEventListener('keydown', handleEscapeKey);
});

const closeModal = () => {
  showModal.value = false;
  resetForm();
};

const resetForm = () => {
  email.value = '';
  code.value = '';
  showCodeInput.value = false;
  errorMessage.value = '';
  emailLoading.value = false;
  codeLoading.value = false;
};

const handleGoogleLogin = async () => {
  try {
    await signInWithGoogle();
  } catch (error: any) {
    errorMessage.value = error.message || 'Failed to sign in with Google';
  }
};

const handleEmailLogin = async () => {
  if (!email.value) return;
  
  emailLoading.value = true;
  errorMessage.value = '';
  
  try {
    const response = await createPasswordlessCode(email.value);
    if (response.status === 'OK') {
      showCodeInput.value = true;
    }
  } catch (error: any) {
    errorMessage.value = error.message || 'Failed to send verification code';
  } finally {
    emailLoading.value = false;
  }
};

const handleCodeVerification = async () => {
  if (code.value.length !== 6) return;
  
  codeLoading.value = true;
  errorMessage.value = '';
  
  try {
    const response = await consumePasswordlessCode(code.value);
    
    if (response.status === 'OK') {
      // Check if this is a new user
      if (response.createdNewRecipeUser) {
        try {
          const apiDomain = import.meta.env.VITE_API_DOMAIN || 'http://localhost:8123';
          await fetch(`${apiDomain}/api/v1/user/register`, {
            method: 'PUT',
            credentials: 'include',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              email: response.user.emails[0]
            })
          });
        } catch (regError) {
          console.error('Failed to register user:', regError);
        }
      }
      
      closeModal();
      // Router guard will redirect based on onboarding status
      router.push('/');
    } else if (response.status === 'INCORRECT_USER_INPUT_CODE_ERROR') {
      errorMessage.value = 'Invalid code. Please try again.';
    } else if (response.status === 'EXPIRED_USER_INPUT_CODE_ERROR') {
      errorMessage.value = 'Code expired. Please request a new one.';
    } else {
      errorMessage.value = 'Verification failed. Please try again.';
    }
  } catch (error: any) {
    errorMessage.value = error.message || 'Failed to verify code';
  } finally {
    codeLoading.value = false;
  }
};

const handleResendCode = async () => {
  if (resendCooldown.value > 0) return;
  
  try {
    await resendPasswordlessCode();
    errorMessage.value = '';
    
    // Start cooldown
    resendCooldown.value = 30;
    const interval = setInterval(() => {
      resendCooldown.value--;
      if (resendCooldown.value <= 0) {
        clearInterval(interval);
      }
    }, 1000);
  } catch (error: any) {
    errorMessage.value = error.message || 'Failed to resend code';
  }
};
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.2s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}
</style>
