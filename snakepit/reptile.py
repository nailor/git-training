def is_reptile(reptile):
    if reptile is 'worm':
        return False
    return True


def snake(entity=None):
    print "It's a snaaaake, snaaaake"


def viper():
    snake(entity='viper')


def honeybadger(snake):
    print 'Eating %s' % snake
