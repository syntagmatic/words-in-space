var Poem = Backbone.Model.extend({
  defaults: function() {
    return {
      text: "to be or not to be"
    }
  },
});

var PoemList = Backbone.Collection.extend({
  model: Poem,
  localStorage: new Store("poems-backbone")
});

var Poems = new PoemList;

Poems.fetch();
