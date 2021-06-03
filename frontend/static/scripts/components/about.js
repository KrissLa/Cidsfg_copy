document.querySelector('#video-preview').addEventListener('click', e => {
    e.target.style.display = 'none';
    const videoDiv = `<div class="entry-video embed-responsive embed-responsive-16by9">
                        <video controls autoplay>
                            <source src="/static/video/Rolik_zavod.mp4" type="video/mp4">
                        </video>
                    </div>`;
    e.target.parentNode.insertAdjacentHTML('afterbegin', videoDiv);
})