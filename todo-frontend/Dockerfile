# Step 1: Build React app
FROM node:18 AS build

WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# Step 2: Serve with Nginx
FROM nginx:alpine

# Copy build files
COPY --from=build /app/build /usr/share/nginx/html

# 👇 IMPORTANT: copy nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf