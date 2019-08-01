import React from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { newMessage } from '../modules/game';

class ChatBox extends React.Component {
  state = {
    message: '',
  };

  componentDidUpdate() {
    this.scrollToBottom();
  }

  scrollToBottom = () => {
    this.messagesEnd.scrollIntoView({ behavior: 'smooth' });
  };

  handleChange = (e) => {
    const { value } = e.target;
    this.setState({ message: value });
  };

  handleSubmit = () => {
    const { dispatch } = this.props;
    const { message } = this.state;
    dispatch(newMessage(message));
    this.setState({ message: '' });
  };

  onKeyPress = (e) => {
    if (e.key === 'Enter') {
      this.handleSubmit();
    }
  };

  render() {
    const { message } = this.state;
    const { game } = this.props;
    return (
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          background: '#70d6ff',
          boxShadow: '0 2px 10px 0 rgba(0, 0, 0, 0.5), inset 0 1px 3px 0 rgba(0, 0, 0, 0.5)',
          borderRadius: '20px',
          marginRight: '1%',
          marginLeft: '1%',
          marginBottom: '1%',
          marginTop: '2%',
          padding: '2%',
          maxHeight: '500px',
          width: '25%',
        }}
      >
        <div
          style={{
            overflowY: 'scroll',
            marginRight: '2px',
            minHeight: '350px',
            maxHeight: '350px',
          }}
        >
          {game
            && game.messages.map(msg => (
              <div key={msg.id}>
                <span>
                  {' '}
                  {msg.message_type === 'action' ? null : `${msg.username}: `}
                  {msg.message}
                </span>
              </div>
            ))}
          <div
            style={{ float: 'left', clear: 'both' }}
            ref={(el) => {
              this.messagesEnd = el;
            }}
          />
        </div>
        <div
          style={{
            display: 'flex',
            marginTop: '5px',
            width: '100%',
          }}
        >
          <input
            style={{ width: '68%', marginRight: '5px' }}
            onChange={this.handleChange}
            value={message}
            onKeyPress={this.onKeyPress}
          />
          <button style={{ width: '20%' }} type="button" onClick={this.handleSubmit}>
            send
            {' '}
          </button>
        </div>
      </div>
    );
  }
}

ChatBox.propTypes = {
  dispatch: PropTypes.func.isRequired,
  game: PropTypes.shape({
    id: PropTypes.number.isRequired,
    game_status: PropTypes.string.isRequired,
    is_joinable: PropTypes.bool.isRequired,
    room_name: PropTypes.string.isRequired,
    round_started: PropTypes.bool.isRequired,
    users: PropTypes.arrayOf(
      PropTypes.shape({
        id: PropTypes.number.isRequired,
        followers: PropTypes.number.isRequired,
        stories: PropTypes.number.isRequired,
        username: PropTypes.string.isRequired,
        started: PropTypes.bool.isRequired,
      }),
    ),
    messages: PropTypes.arrayOf(
      PropTypes.shape({
        id: PropTypes.number.isRequired,
        username: PropTypes.string.isRequired,
        message: PropTypes.string.isRequired,
        message_type: PropTypes.string.isRequired,
        created_at: PropTypes.string.isRequired,
      }),
    ),
  }),
};

ChatBox.defaultProps = {
  game: PropTypes.null,
};

export default connect()(ChatBox);
