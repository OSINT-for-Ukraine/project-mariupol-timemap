import pkg from 'json-server';
import auth from 'json-server-auth'
const { create, router: _router, defaults } = pkg;

// const cert = fs.readFileSync('.cert/certificate.crt');
// const ca = fs.readFileSync('.cert/cabundle.crt');
// const key = fs.readFileSync('.cert/certificate.key');
// let options = {
//    cert: cert, // fs.readFileSync('./ssl/example.crt');
//    ca: ca, // fs.readFileSync('./ssl/example.ca-bundle');
//    key: key // fs.readFileSync('./ssl/example.key');
// };
//
// const server = create(options);
const server = create();
const router = _router('list_of_events.json');
const middlewares = defaults();

server.db = router.db

const rules = auth.rewriter({
  // Permission rules
  users: 600,
  Events: 440,
  Associations: 440,
  Sources: 440
  // Other rules
})

server.use(middlewares);
server.use(rules)
server.use(auth)
server.use(router);

const PORT = 3000; // Change the port if needed
// const fs = require('fs');

server.listen(PORT, () => {
  console.log(`JSON Server is running on port ${PORT}`);
});