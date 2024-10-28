const graphiql = require("graphql");
const {
  GraphQLObjectType,
  GraphQLString,
  GraphQLInt,
  GraphQLSchema,
  GraphQLList,
  GraphQLNonNull,
} = graphiql;

const userType = new GraphQLObjectType({
  name: "user",
  fields: () => ({
    id: { type: GraphQLInt },
    name: { type: GraphQLString },
    email: { type: GraphQLString },
    PhoneNo: { type: GraphQLInt },
  }),
});

let RootQuery = new GraphQLObjectType({
  name: "xyz",
  fields: {
    usertest: {
      type: new GraphQLList(userType),

      resolve(parentValue, args) {
        let data = [
          {
            id: 1,
            name: "John",
            email: "john@com",
            PhoneNo: 1234567890,
          },
          {
            id: 2,
            name: "Doe",
            email: "Doe@com",
            PhoneNo: 9004567890,
          },
        ];
        return data;
      },
    },
    usertest1: {
      type: new GraphQLList(userType),

      resolve(parentValue, args) {
        let data = [
          {
            id: 1,
            name: "John1",
            email: "john@com",
            PhoneNo: 1234567890,
          },
          {
            id: 2,
            name: "Doe1",
            email: "Doe@com",
            PhoneNo: 9004567890,
          },
        ];
        return data;
      },
    },
  },
});

module.exports = new GraphQLSchema({ query: RootQuery });
