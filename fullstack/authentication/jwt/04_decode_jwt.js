/*
URL: https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/2baeea23-aa82-4c96-aaf9-670855db2b70/concepts/02439724-158d-4bc3-baf0-674ef2b2a81e

Chapter 4. Identity and Access Management
Lesson 4: Access and Authorization
Part 5: Restricting Features in Frontend
Comment: Use "" as string argument in the function call. e.g. parseJwt("token_string")
*/

function parseJwt (token) {
    // https://stackoverflow.com/questions/38552003/how-to-decode-jwt-token-in-javascript
   var base64Url = token.split('.')[1];
   var base64 = decodeURIComponent(atob(base64Url).split('').map((c)=>{
       return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
   }).join(''));

   return JSON.parse(base64);
};