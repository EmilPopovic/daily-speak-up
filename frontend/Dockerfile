# Build stage
FROM node:22-alpine AS builder

WORKDIR /app

# Add build arguments
ARG VITE_AUTH0_DOMAIN
ARG VITE_AUTH0_CLIENT_ID

COPY package*.json ./

RUN npm install

COPY . .

# Create the runtime config before build
RUN echo "window.ENV = { \
    VITE_AUTH0_DOMAIN: '${VITE_AUTH0_DOMAIN}', \
    VITE_AUTH0_CLIENT_ID: '${VITE_AUTH0_CLIENT_ID}' \
};" > public/env.js

RUN npm run build

# Production stage
FROM node:22-alpine

WORKDIR /app

RUN npm install -g serve && \
    apk add --no-cache curl

COPY --from=builder /app/dist ./dist

EXPOSE 3000

CMD ["serve", "-s", "dist", "-l", "3000"]
