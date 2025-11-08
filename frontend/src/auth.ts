import { createAuth0Client, Auth0Client } from '@auth0/auth0-spa-js';

let clientPromise: Promise<Auth0Client> | null = null;

function getClient(): Promise<Auth0Client> {
  if (!clientPromise) {
    clientPromise = createAuth0Client({
      domain: import.meta.env.VITE_AUTH0_DOMAIN,
      clientId: import.meta.env.VITE_AUTH0_CLIENT_ID,
      authorizationParams: {
        audience: import.meta.env.VITE_AUTH0_AUDIENCE,
        redirect_uri: import.meta.env.VITE_AUTH0_REDIRECT_URI
      },
      cacheLocation: 'localstorage',
      useRefreshTokens: true
    });
  }
  return clientPromise;
}

export async function handleRedirectCallbackIfPresent() {
  const client = await getClient();
  const qp = new URLSearchParams(window.location.search);
  if (qp.has('code') && qp.has('state')) {
    await client.handleRedirectCallback();
    window.history.replaceState({}, document.title, '/');
  }
}

export async function login() {
  const client = await getClient();
  await client.loginWithRedirect();
}

export async function logout() {
  const client = await getClient();
  client.logout({ logoutParams: { returnTo: window.location.origin } });
}

export async function isAuthenticated(): Promise<boolean> {
  const client = await getClient();
  return client.isAuthenticated();
}

export async function getAccessToken(): Promise<string | null> {
  const client = await getClient();
  try {
    return await client.getTokenSilently();
  } catch {
    return null;
  }
}

export async function getUser(): Promise<any | null> {
  const client = await getClient();
  try {
    return await client.getUser();
  } catch {
    return null;
  }
}
