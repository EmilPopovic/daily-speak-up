import Session from 'supertokens-web-js/recipe/session';
import ThirdParty from 'supertokens-web-js/recipe/thirdparty';

export async function signInWithGoogle() {
  try {
    const authUrl = await ThirdParty.getAuthorisationURLWithQueryParamsAndSetState({
      thirdPartyId: 'google',
      frontendRedirectURI: `${window.location.origin}/auth/callback/google`
    });
    
    // Redirect to Google OAuth
    window.location.assign(authUrl);
  } catch (err) {
    console.error('Error initiating Google sign-in:', err);
    throw err;
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
