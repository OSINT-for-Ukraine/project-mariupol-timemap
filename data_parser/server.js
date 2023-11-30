
import pkg from 'json-server';
const { create, router: _router, defaults } = pkg;

const server = create();
const router = _router('list_of_events.json');
const middlewares = defaults();

server.use(middlewares);
server.use(router);

const PORT = 3000; // Change the port if needed

server.listen(PORT, () => {
  console.log(`JSON Server is running on port ${PORT}`);
});