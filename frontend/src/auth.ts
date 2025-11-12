import Session from 'supertokens-web-js/recipe/session';
import EmailPassword from 'supertokens-web-js/recipe/emailpassword';

export async function signUp(email: string, password: string) {
  try {
    const response = await EmailPassword.signUp({
      formFields: [{
        id: "email",
        value: email
      }, {
        id: "password",
        value: password
      }]
    });

    if (response.status === "OK") {
      return { success: true, user: response.user };
    } else if (response.status === "FIELD_ERROR") {
      const errors = response.formFields.map(f => f.error).filter(Boolean).join(', ');
      return { success: false, error: errors || "Sign up failed" };
    } else {
      return { success: false, error: "Sign up failed" };
    }
  } catch (error) {
    return { success: false, error: "An error occurred during sign up" };
  }
}

export async function signIn(email: string, password: string) {
  try {
    const response = await EmailPassword.signIn({
      formFields: [{
        id: "email",
        value: email
      }, {
        id: "password",
        value: password
      }]
    });

    if (response.status === "OK") {
      return { success: true, user: response.user };
    } else if (response.status === "WRONG_CREDENTIALS_ERROR") {
      return { success: false, error: "Invalid email or password" };
    } else {
      return { success: false, error: "Sign in failed" };
    }
  } catch (error) {
    return { success: false, error: "An error occurred during sign in" };
  }
}

export async function logout() {
  await Session.signOut();
  window.location.href = '/';
}

export async function isAuthenticated(): Promise<boolean> {
  return await Session.doesSessionExist();
}

export async function getUserId(): Promise<string | undefined> {
  if (await Session.doesSessionExist()) {
    return await Session.getUserId();
  }
  return undefined;
}

// For backward compatibility with existing code
export async function getAccessToken(): Promise<string | null> {
  // SuperTokens handles auth via cookies, no need for access tokens
  return null;
}

export async function getUser(): Promise<any | null> {
  if (await Session.doesSessionExist()) {
    const userId = await Session.getUserId();
    return { id: userId };
  }
  return null;
}
