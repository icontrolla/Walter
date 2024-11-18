let likeCount = 0;

document.getElementById('like-button').addEventListener('click', function() {
    likeCount++;
    document.getElementById('like-count').innerText = likeCount + ' flowers';
});