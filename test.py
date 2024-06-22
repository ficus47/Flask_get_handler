import tensorflow as tf

# Charger le modèle SavedModel
model = tf.saved_model.load("model_tf")

# Afficher les signatures disponibles
print(model.signatures)

# Supposons que vous voulez inspecter une signature spécifique nommée 'serving_default'
signature = model.signatures['serving_default']

# Afficher les détails des entrées et des sorties de la signature 'serving_default'
print(signature.inputs)
print(signature.outputs)

# Maintenant, vous pouvez voir les noms des sorties disponibles dans cette signature
# Utilisez le nom approprié pour accéder à la sortie dont vous avez besoin dans votre application
