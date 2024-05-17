import os  # Importa o módulo os para interagir com o sistema operacional
import cv2  # Importa o OpenCV para manipulação de imagens

# Lê a imagem da impressão digital alterada para ser usada como amostra
sample = cv2.imread("SOCOFing/Altered/Altered-Hard/150__M_Right_index_finger_Obl.BMP")

# Inicializa variáveis para armazenar o melhor resultado de correspondência
best_score = 0
filename = None
image = None
kp1, kp2, mp = None, None, None

# Itera por cada arquivo na pasta de impressões digitais reais
for file in os.listdir("SOCOFing/Real"):
    # Lê a imagem de impressão digital atual
    fingerprint_image = cv2.imread("SOCOFing/Real/" + file)
    sift = cv2.SIFT_create()  # Cria um objeto SIFT (Scale-Invariant Feature Transform)

    # Detecta e computa os descritores de características da amostra e da imagem de impressão digital atual
    keypoints_1, descriptors_1 = sift.detectAndCompute(sample, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None)

    # Encontra os correspondentes usando o FlannBasedMatcher
    matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10}, {}).knnMatch(descriptors_1, descriptors_2, k=2)

    match_points = []  # Lista para armazenar os pontos correspondentes válidos

    # Filtra as correspondências com base na distância
    for p, q in matches:
        if p.distance < 0.1 * q.distance:
            match_points.append(p)

    # Determina o número de pontos chave
    keypoints = min(len(keypoints_1), len(keypoints_2))

    # Atualiza a melhor pontuação se a pontuação atual for maior
    if len(match_points) / keypoints * 100 > best_score:
        best_score = len(match_points) / keypoints * 100
        filename = file
        image = fingerprint_image
        kp1, kp2, mp = keypoints_1, keypoints_2, match_points

# Imprime o melhor resultado de correspondência
print("BEST MATCH: " + filename)
print("SCORE: " + str(best_score))

# Desenha as correspondências na imagem de resultado
result = cv2.drawMatches(sample, kp1, image, kp2, mp, None, flags=2)

# Redimensiona a imagem para melhor visualização
result = cv2.resize(result, None, fx=4, fy=4)

# Exibe a imagem de resultado
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()