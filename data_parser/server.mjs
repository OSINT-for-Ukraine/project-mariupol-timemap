import pkg from 'json-server';
import auth from 'json-server-auth'
const { create, router: _router, defaults } = pkg;


const server = create();
const router = _router('api.json');
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