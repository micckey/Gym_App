import random

quotesList = {
    0: '"The purpose of training is to tighten up the slack, toughen the body, and polish the spirit.¨ - Morihei Ueshiba',

    1: '¨The only person you are destined to become is the person you decide to be.¨ – Ralph Waldo Emerson',

    2: '"Once you learn to quit, it becomes a habit.¨ ― Vince Lombardi Jr',

    3: '¨A year from now you may wish you had started today.¨ – Karen Lamb',

    4: '¨Our growing softness, our increasing lack of physical fitness, is a menace to our security.¨— John F. Kennedy',

    5: '¨Don’t give up on your dreams, or your dreams will give up on you.¨ – John Wooden',

    6: '“The last three or four reps is what makes the muscle grow. This area of pain divides a champion from someone who is not a champion.”- Arnold Schwarzenegger',

    7: '¨Most people fail, not because of lack of desire, but, because of lack of commitment.¨ – Vince Lombardi',

    8: '“Success usually comes to those who are too busy to be looking for it.” -Henry David Thoreau',

    9: '"Exercise is labor without weariness.¨ - Samuel Johnson',

    10: '¨Some people want it to happen, some wish it would happen, others make it happen.¨ – Michael Jordan Unsplash',

    11: '"The first time I see a jogger smiling, I''ll consider it.¨- Joan Rivers',

    12: '“All progress takes place outside the comfort zone.”- Michal Joan Bobak',

    13: '¨Look in the mirror. That’s your competition.¨ – John Assaraf',

    14: '¨Tough times don’t last. Tough people do.¨ – Robert H. Schuller',

    15: '¨A feeble body weakens the mind.¨ - Jean-Jacques Rousseau',

    16: '¨Put all excuses aside and remember this: You are capable.¨ – Zig Ziglar',

    17: '¨Bodybuilding is much like any other sport. To be successful, you must dedicate yourself 100% to your training, diet and mental approach.¨ - Arnold Schwarzenegger',

    18: '¨If we could give every individual the right amount of nourishment and exercise, not too little and not too much, we would have found the safest way to health.¨ — Hippocrates',

    19: '"Swimming is normal for me. I''m relaxed. I''m comfortable, and I know my surroundings. It''s my home.¨- Michael Phelps',

    20: '“If you think lifting is dangerous, try being weak. Being weak is dangerous.” - Bret Contreras',

    21: '¨There is a moment when you get older when your metabolism slows down and you don''t feel like working out any more, so you don''t want to keep yourself fit any more, but that''s your decision. Why should you be judged for it?¨ - Janet Jackson',

    22: '¨The groundwork for all happiness is good health.¨ – Leigh Hunt',

    23: '“The only place where success comes before work is in the dictionary.”- Vidal Sassoon',

    24: '¨The human body is the best picture of the human soul.¨ - Ludwig Wittgenstein',

    25: '¨Our bodies are our gardens – our wills are our gardeners.¨ – William Shakespeare',

    26: '“The clock is ticking. Are you becoming the person you want to be?” - Greg Plitt',

    27: '¨Reading is to the mind what exercise is to the body.¨- Joseph Addison',

    28: '¨Exercise is king. Nutrition is queen. Put them together and you’ve got a kingdom.¨ – Jack LaLanne',

    29: '¨Physical fitness is not only one of the most important keys to a healthy body, it is the basis of dynamic and creative intellectual activity.¨ – John F. Kennedy',

    30: '“Whether you think you can, or you think you can’t, you’re right.” - Henry Ford Unsplash',

    31: '¨There''s a lot of people in this world who spend so much time watching their health that they haven''t the time to enjoy it.¨- Josh Billings',

}
random_quote = random.choice(quotesList)

descriptionList = {
    1: 'Get down on all fours, placing your hands slightly wider than your shoulders. Straighten your arms and leg. Lower your body until your chest nearly touches the floor. Pause, then push yourself back up. Repeat. ',

    2: 'Grab a handle in each hand and start with the rope behind you, so it\'s right at your heels. To get the rope moving, gently rotate your forearms forward and then your wrists to generate momentum and swing it overhead and jump by springing from your toes. Start slowly so you can master the timing of it. Once you get a few jumps down, you\'ll know when to jump naturally.',

    3: 'The simplest approach of how to ride a bike is simply to get on, press the quick-start button, and adjust the settings until you’re at a comfortable warmup pace.',

    4: 'The simplest approach of how to run on a treadmill for beginners is simply to get on, press the quick-start button, and increase the speed until you’re at a comfortable warmup pace.',

    5: 'Lie on your back on a flat bench. Grip a barbell with hands slightly wider than shoulder width. The bar should be directly over the shoulders. Press your feet firmly into the ground and keep your hips on the bench throughout the entire movement. Keep your core engaged and maintain a neutral spine position throughout the movement. Avoid arching your back. Slowly lift the bar or dumbbells off the rack, if using. Lower the bar to the chest, about nipple level, allowing elbows to bend out to the side, about 45 degrees away from the body. Stop lowering when your elbows are just below the bench. Press feet into the floor as you push the bar back up to return to starting position. Repeat.',

    6: 'Start in a squat position with your knees bent, back straight, and your feet about shoulder-width apart. Lower your hands to the floor in front of you so they’re just inside your feet. With your weight on your hands, kick your feet back so you’re on your hands and toes, and in a pushup position. Keeping your body straight from head to heels, do one pushup. Remember not to let your back sag or to stick your butt in the air. Do a frog kick by jumping your feet back to their starting position. Stand and reach your arms over your head. Jump quickly into the air so you land back where you started. Repeat',

    7: 'Stand behind a barbell with your feet about shoulder-width apart. Sit your hips back, bend your knees slightly, and lean your torso forward, maintaining a tight core and flat back. Grab the bar, placing your hands shoulder-width apart, palms facing in toward your body. Push your feet into the floor and stand up tall, pulling the weight with you and keeping your arms straight. Bring your hips forward and squeeze your abs and glutes at the top. Slowly reverse the movement, bending your knees and pushing your butt back to lower the weight back to the floor. Keep the bar close to your body the entire time and maintain a flat back. Repeat.',

    8: 'Stand tall, still gripping the bell. Keep your arms long and loose while squeezing your shoulder blades together and engaging your core. Soften your knees, shift your body weight into your heels, and lower your butt back and down toward the wall behind you. Driving through your heels, explode through your hips to send the weight swinging upward from your quads. Aim for chest height, with your arms extended. Achieving this finishing position requires you to snap your hips through, contracting your core while squeezing your glutes. As the kettlebell begins to descend, let the weight do the work as you ready your body for the next rep. Shift your weight back into your heels while hinging at your hips and loading both your hamstrings and glutes. Receive the weight of the kettlebell, allowing it to ride back between your legs. As the kettlebell makes the transition from backward to forward, drive through your heels and hips to repeat.',

    9: 'Lie on your back and set your knees about shoulder-width apart, with your feet flat to the ground and your knees bent. Make sure your toes are pointed straight forward and that your heels are 6–8 inches from your glutes. Lay your arms flat on either side of you with your palms open toward the ceiling. Slowly raise your hips, engage your glutes, and squeeze your abs. Be careful not to arch your back as you lift your hips as high as possible. A perfect glute bridge consists of elevating your hips until your torso makes a straight line from your shoulder up to your knee. Once you reach the top of the glute bridge, squeeze your glutes as tightly as possible and hold for a few seconds. Lower your hips back down to the ground in a controlled motion without releasing the tension in your abs and glutes.',

    10: 'Start in a traditional squat stance with your feet about shoulder-width apart and toes pointed forward. Clasp your hands together at your chest. Take a step to the side with your right foot until your stance is wider than hip width. Angle your toes out and away from the center of your body (about 45 degrees). Make sure your knees are still tracking over your toes. Move your hips back slightly and bend your knees as you lower your body into a squat position. Draw your tailbone straight down to the floor. Be mindful to keep your spine neutral, core engaged, and eyes forward throughout the movement. Lower until your thighs are parallel to the floor. You can go lower or shorten the squat if parallel is too low or if you can’t maintain your leg alignment. Pause in the squat position for a few seconds. Then, engaging your glutes, press up to standing, driving up through your heels. Repeat.',

    11: 'Place one leg at a time on top of the stability ball so that the ball is positioned somewhere between the top of your feet (at the ankle joint) and the top of your shins (without interfering with your knees\' ability to bend). The closer to your body the ball is, the easier it will be to maintain your balance. Also, adjust the width of your legs as needed. The closer your feet are together, the more challenging it will be to maintain your balance. Separate your legs slightly for greater stability. Take a breath in when you feel sufficiently balanced, and check your form to make sure your core is engaged and your body forms a straight line from heels to head. Maintain your shoulders over your wrists for the entirety of the movement. Press your feet and shins down into the stability ball and use your abs to help draw the ball toward your chest as you bend your knees and tuck your lower body up to your torso. Bring your knees as close to your chest as you comfortably can. Exhale as you draw your knees forward. Hold for a second, then extend your knees, rolling the stability ball away from your torso to return to the full plank position. Exhale as you roll the ball away from you. Repeat.',

    12: 'Sit up tall and relax your neck and shoulders. Your feet should be flat on the floor. Grab the handles so that your palms are facing forward. Note that some machines have a foot bar that you need to push in order to release the handles and bring them forward. Press your arms together in front of your chest with a slow, controlled movement. Keep a slight, soft bend in the elbows with wrists relaxed. Pause for one second once your arms are fully "closed" in front of your chest. Bring your arms slowly back to the starting position, opening your chest and keeping posture strong and upright. Repeat.',

    13: 'Sit tall on the rowing machine with your arms straight, back upright, and knees and ankles flexed so that your shins are roughly vertical. From this position, use your lats to pull your shoulders down and brace your core. This engagement will help protect your lower back. Then lean forward slightly, keeping your back tall. Begin by pushing with your legs, while still bracing and contracting your core. When your legs are straight, hinge at the hips and lean back to about 45 degrees. The last movement is from your arms as you pull the handle towards your torso, a few inches above your belly button. Note the order of body movements: legs, core, hips and shoulders, arms. This is the resting position opposite the catch position—although you won\'t rest here for long. Legs are long, shoulders and back are leaning away from the legs, hands (and handle) are pulled in toward the body, and elbows are tucked in toward the torso.Now do the drive movements in reverse order to return to the catch position. Extend the arms, hinge the hips forward to bring the torso over the legs, then bend the knees. Repeat.',

    14: 'Brace your abdominal muscles and push the platform away with your heels and forefoot.Your heels should remain flat on the footplate. The front of your foot or toes should never be used exclusively to move the pad forward. While exhaling, extend your legs and keep your head and back flat against the seat pad. Extend with slow control rather than with an explosive movement. Pause at the top of the movement. Do not lock out your knees, and ensure that they are not bowing out or in. While inhaling, return the footplate to the starting position by gradually bending the knees. Keep the feet and back flat throughout. Repeat.',

    15: 'Stand with feet hips-width apart and knees soft, holding dumbbells in front of hips with palms facing thighs. Keeping spine in neutral position and squeezing shoulder blades, start sending hips back. Lower dumbbells in front of shins, keeping them close to the body. Once the dumbbells pass the knees, do not allow the hips to sink further. At the bottom of the movement, maintain a neutral spine and drive through heels to fully extend hips and knees, squeezing glutes at the top of the movement. Repeat.',

    16: 'Stand with your feet hip- to shoulder-width apart, holding a dumbbell in each hand. Brace your core, push your hips back, bend your knees slightly, and lower your torso until it’s nearly parallel to the floor. Let the dumbbells hang at arms length with your palms facing back. Engage your shoulder blades to keep your shoulders pulled back (i.e., don’t hunch). This is the starting position. Without moving your torso, and while keeping your elbows tucked and back flat, row the weights to your sides as you squeeze your shoulder blades together. Pause, and then lower the weights back to the starting position.',

    17: 'Stand upright and keep the back straight. Hold a dumbbell in each hand, at the shoulders, with an overhand grip. Thumbs are on the inside and knuckles face up. Exhale as you raise the weights above the head in a controlled motion. Pause briefly at the top of the motion. Inhale and return the dumbbells to the shoulders.',

    18: 'Put a bench in a decline position. Start at around 30 degrees to see how it feels and go from there. Lie on the bench and secure your legs on the knee and ankle pads. With your back against the bench, bring your hands to the sides of your head and take a breath. Initiate the crunch by engaging your abs and using them to lift your torso toward your thighs. Raise your torso as you simultaneously crunch in for maximum abdominal engagement. Your chest should come near to your knees at the top position. Hold the top position for a moment and slowly lower your torso back to the starting position. Take another breath and repeat.',

}

avocado = "assets/avocado.jpg"
avocado2 = "assets/avocado2.webp"
avocado3 = "assets/avocado3.webp"
burrito = "assets/Burrito.webp"
eggs = "assets/eggs.jpg"
greens = "assets/greens.webp"
oats = "assets/oats.jpeg"
salmon = "assets/salmon.webp"

foodsList = {
    0: avocado,
    1: avocado2,
    2: avocado3,
    3: burrito,
    4: eggs,
    5: greens,
    6: oats,
    7: salmon
}
random_food = random.choice(foodsList)