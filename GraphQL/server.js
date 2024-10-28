const express = require("express");
const app = express();
const PORT = 3333;
const { graphqlHTTP } = require("express-graphql");

const schema = require("./schema");

app.use(express.json());

app.use(
  "/graphQL",
  graphqlHTTP({
    schema: schema,
    graphiql: true,
  })
);

app.listen(PORT, () => {
  console.log(`Server is running on port http://localhost:${PORT}`);
});
